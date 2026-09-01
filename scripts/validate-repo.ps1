[CmdletBinding()]
param(
    [switch]$Strict
)

$ErrorActionPreference = 'Stop'

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
Set-Location -LiteralPath $RepoRoot

$errors = New-Object System.Collections.Generic.List[string]
$warnings = New-Object System.Collections.Generic.List[string]

function Add-ValidationError {
    param([string]$Message)
    $errors.Add($Message) | Out-Null
}

function Add-ValidationWarning {
    param([string]$Message)
    $warnings.Add($Message) | Out-Null
}

function Get-RepoRelativePath {
    param([string]$Path)
    $resolved = (Resolve-Path -LiteralPath $Path).Path
    if ($resolved.StartsWith($RepoRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
        return $resolved.Substring($RepoRoot.Length).TrimStart('\', '/')
    }
    return $resolved
}

function Test-Heading {
    param(
        [string]$Text,
        [string]$Heading
    )
    $pattern = '(?m)^##\s+' + [regex]::Escape($Heading) + '\s*$'
    return [regex]::IsMatch($Text, $pattern)
}

$requiredSkillHeadings = @(
    'When to Use This Skill',
    "What You'll Need to Provide",
    'Mission',
    'Strategy',
    'Output Format',
    'Quality Checks',
    'When Data is Missing',
    'Confidence Scoring',
    'Related Knowledge Bases'
)

$rootSkillDir = Join-Path $RepoRoot 'skills'
$pluginDir = Join-Path $RepoRoot 'claude-code-plugins'
$knowledgeDir = Join-Path $RepoRoot 'knowledge'
$researchDir = Join-Path $RepoRoot 'research'

$rootSkills = @(Get-ChildItem -LiteralPath $rootSkillDir -Recurse -File -Filter '*.md')
$rootSkillsByName = @{}

foreach ($skill in $rootSkills) {
    if ($rootSkillsByName.ContainsKey($skill.Name)) {
        Add-ValidationError "Duplicate root skill filename '$($skill.Name)' at $(Get-RepoRelativePath $skill.FullName) and $(Get-RepoRelativePath $rootSkillsByName[$skill.Name].FullName)."
    }
    else {
        $rootSkillsByName[$skill.Name] = $skill
    }
}

foreach ($skill in $rootSkills) {
    $relative = Get-RepoRelativePath $skill.FullName
    $text = Get-Content -LiteralPath $skill.FullName -Raw

    foreach ($heading in $requiredSkillHeadings) {
        if (-not (Test-Heading -Text $text -Heading $heading)) {
            Add-ValidationError "$relative is missing required heading '## $heading'."
        }
    }

    $mirrors = @(Get-ChildItem -LiteralPath $pluginDir -Recurse -File -Filter $skill.Name | Where-Object {
        $_.FullName -match '[\\/]skills[\\/]'
    })
    if ($mirrors.Count -eq 0) {
        Add-ValidationError "$relative has no Claude Code plugin mirror."
    }
}

$plugins = @(Get-ChildItem -LiteralPath $pluginDir -Directory)
foreach ($plugin in $plugins) {
    $skillEntry = Join-Path $plugin.FullName 'SKILL.md'
    if (-not (Test-Path -LiteralPath $skillEntry)) {
        Add-ValidationError "$(Get-RepoRelativePath $plugin.FullName) is missing SKILL.md."
    }

    $pluginSkills = @(Get-ChildItem -LiteralPath $plugin.FullName -Recurse -File -Filter '*.md' | Where-Object {
        $_.FullName -match '[\\/]skills[\\/]'
    })
    foreach ($pluginSkill in $pluginSkills) {
        if (-not $rootSkillsByName.ContainsKey($pluginSkill.Name)) {
            Add-ValidationError "$(Get-RepoRelativePath $pluginSkill.FullName) has no root skill with matching filename."
            continue
        }
        $rootSkill = $rootSkillsByName[$pluginSkill.Name]
        $mirrorHash = (Get-FileHash -LiteralPath $pluginSkill.FullName -Algorithm SHA256).Hash
        $rootHash = (Get-FileHash -LiteralPath $rootSkill.FullName -Algorithm SHA256).Hash
        if ($mirrorHash -ne $rootHash) {
            Add-ValidationError "$(Get-RepoRelativePath $pluginSkill.FullName) differs from $(Get-RepoRelativePath $rootSkill.FullName); root is the source of truth, copy it over the mirror."
        }
    }

    $pluginKnowledge = @(Get-ChildItem -LiteralPath $plugin.FullName -Recurse -File -Filter '*.md' | Where-Object {
        $_.FullName -match '[\\/]knowledge[\\/]'
    })
    foreach ($knowledgeCopy in $pluginKnowledge) {
        $rootKnowledge = Join-Path $knowledgeDir $knowledgeCopy.Name
        if (-not (Test-Path -LiteralPath $rootKnowledge)) {
            Add-ValidationError "$(Get-RepoRelativePath $knowledgeCopy.FullName) has no root knowledge file with matching filename."
        }
    }
}

if (Test-Path -LiteralPath $researchDir) {
    $researchAreas = @(Get-ChildItem -LiteralPath $researchDir -Directory)
    foreach ($area in $researchAreas) {
        $indexPath = Join-Path $area.FullName 'INDEX.md'
        if (-not (Test-Path -LiteralPath $indexPath)) {
            Add-ValidationError "$(Get-RepoRelativePath $area.FullName) is missing INDEX.md."
        }

        $skillArea = Join-Path $rootSkillDir $area.Name
        if (Test-Path -LiteralPath $skillArea) {
            foreach ($skill in @(Get-ChildItem -LiteralPath $skillArea -File -Filter '*.md')) {
                $expectedResearch = Join-Path $area.FullName ("{0}-research.md" -f [IO.Path]::GetFileNameWithoutExtension($skill.Name))
                if (-not (Test-Path -LiteralPath $expectedResearch)) {
                    Add-ValidationError "$(Get-RepoRelativePath $skill.FullName) is in a research-backed area but lacks $(Get-RepoRelativePath $expectedResearch)."
                }
            }
        }
    }
}

$readmePath = Join-Path $RepoRoot 'README.md'
if (Test-Path -LiteralPath $readmePath) {
    $readme = Get-Content -LiteralPath $readmePath -Raw
    $knowledgeCount = @(Get-ChildItem -LiteralPath $knowledgeDir -File -Filter '*.md').Count
    $pluginCount = $plugins.Count
    $researchNoteCount = @(Get-ChildItem -LiteralPath $researchDir -Recurse -File -Filter '*.md' | Where-Object {
        $_.Name -ne 'INDEX.md'
    }).Count

    $badgeExpectations = @(
        @{ Label = 'Skills'; Pattern = 'Skills-(\d+)'; Actual = $rootSkills.Count },
        @{ Label = 'Knowledge_Bases'; Pattern = 'Knowledge_Bases-(\d+)'; Actual = $knowledgeCount },
        @{ Label = 'Research_Notes'; Pattern = 'Research_Notes-(\d+)'; Actual = $researchNoteCount },
        @{ Label = 'Claude_Code_Plugins'; Pattern = 'Claude_Code_Plugins-(\d+)'; Actual = $pluginCount }
    )

    foreach ($expectation in $badgeExpectations) {
        $match = [regex]::Match($readme, $expectation.Pattern)
        if (-not $match.Success) {
            Add-ValidationWarning "README badge for $($expectation.Label) was not found."
            continue
        }

        $declared = [int]$match.Groups[1].Value
        if ($declared -ne $expectation.Actual) {
            Add-ValidationError "README badge $($expectation.Label) declares $declared but repo has $($expectation.Actual)."
        }
    }
}

# Attribution: every skill file must carry the frontmatter + footer stamped by scripts/add_attribution.py
$attributionCopyright = 'Copyright 2026 Avi Hacker, J.D. / The AI Consulting Network'
$attributionFiles = @($rootSkills) + @(Get-ChildItem -LiteralPath $pluginDir -Recurse -File -Filter '*.md' | Where-Object {
    $_.FullName -match '[\\/]skills[\\/]' -or $_.Name -eq 'SKILL.md'
})
foreach ($file in $attributionFiles) {
    $text = Get-Content -LiteralPath $file.FullName -Raw
    $gaps = @()
    $fm = [regex]::Match($text, '\A---\r?\n(.*?)\r?\n---\r?\n', [System.Text.RegularExpressions.RegexOptions]::Singleline)
    if (-not ($fm.Success -and $fm.Groups[1].Value.Contains('license: Apache-2.0') -and $fm.Groups[1].Value.Contains($attributionCopyright))) {
        $gaps += 'frontmatter'
    }
    $footerIndex = $text.IndexOf('## Attribution')
    if ($footerIndex -lt 0 -or -not $text.Substring($footerIndex).Contains($attributionCopyright)) {
        $gaps += 'footer'
    }
    if ($gaps.Count -gt 0) {
        Add-ValidationError "$(Get-RepoRelativePath $file.FullName) lacks attribution $($gaps -join ' and '); run scripts/add_attribution.py."
    }
}

if ($warnings.Count -gt 0) {
    Write-Host 'Validation warnings:'
    foreach ($warning in $warnings) {
        Write-Host "  - $warning"
    }
}

if ($errors.Count -gt 0) {
    Write-Host 'Validation errors:'
    foreach ($validationError in $errors) {
        Write-Host "  - $validationError"
    }
    exit 1
}

Write-Host "Validation passed: $($rootSkills.Count) skills, $(@(Get-ChildItem -LiteralPath $knowledgeDir -File -Filter '*.md').Count) knowledge bases, $($plugins.Count) plugins."
if ($Strict) {
    Write-Host 'Strict mode enabled.'
}
