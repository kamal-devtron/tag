
# Enterprise Release

Please follow the below instructions for PR:

### Title of PR

Type of change: Title / Feature

- docs - The PR contains Documentation ONLY changes. 
- feat - The PR contains new feature/enhancements.
- fix - The PR contains a bug fix.
- chore - Development changes related to the build system (involving scripts, configurations or tools) and package dependencies.
- test - Development changes related to tests.
- perf - Changes related to performance improvements.

Example Title: 
feat: Functionality to observe cost at cluster level

## Section below is for PR description

### 1. PR Links

Include all the relevant PR links in a list format
Example:
- https://github.com/devtron-labs/devtron/pull/123

### 2. Microservices

- [ ] Orchestrator
- [ ] Dashboard
- [ ] Kubelink
- [ ] Kubewatch
- [ ] Casbin
- [ ] Git-sensor
- [ ] Image Scanner
- [ ] Notifier
- [ ] CI-Runner
- [ ] Central-API
- [ ] Lens
- [ ] App-Sync

Mark [x] before microservice name to select it

### 3. Additional Release Instructions

Specify any instructions that you want to include in release note, For example:

- [x] Migration Required
- [x] Change in package.json (Include changes in additional comments)

### 4. Migration branch and git hash

Please include the migartion in the below format
<microservice>:<branch-name>/<complete-git-hash>

Example:
orchestrator:fix-issue-12345/067a30dac6436140d284f42804bb72d7756381b2
git-sensor:fix-issue-10000/067a30dac6436140d284f42804bb72d7756381b1

### 4. What channels is this release for?

Specify this release is for which target group

- [ ] OSS+Enterprise
- [ ] Enterprise only
- [ ] Custom enterprise

### 5. Is this a MAJOR release?

If a release is marked MAJOR, additional PR approval from respective code-owners is required. Write the below line if release is major.

Yes <@800718775883268117> <@915555407949348875> <@983236983583293510>

### 6. PR Checklist:

Cross check if you have followed all the required steps

- [x] PR has relevant title tag (feat, fix, perf, chore)
- [x] Is this PR synced to enterprise?

### 7. Release Cluster?

Specify to which cluster you want to release

- [ ] All clusters
- [ ] Staging only
- [ ] CD only
- [ ] Staging and CD

### 8. Author's Github username

Example:
@prakarsh-dt,@vikram-dt

### 9. Additional Comments

Anything else you want to specify, it can be related to additional release instructions as well

