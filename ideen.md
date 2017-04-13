# Ideen

Alle davon sollten für Blogposts oder Lightning Talks gut sein

## git

 * git aliase / usability hacks
    * git root
    * git trash
    * git clean
 * git log enhancements
    * git log & modes & hacks
    * git log --since='2 weeks ago'
    * git log --first-parent: only root and merges
 * using logs logs
    * git log --no-merges --stat --reverse master..: all commits since diverging from master
    * git cherry -v master [<to-be-merged>]: commits not yet merged in master
    * git branch -a --contains <commit-ish>: which branches contain commit
    * git name-rev --name-only <SHA-1>: check if sha-1 was part of release
    * git log --first-parent: only root and merges
    * git checkout master && git branch --no-merged
 * Too little known git commands
    * git grep!!
    * git bundle
 * Too little known git options
    * git branch -vv
    * git branch --no-merged
    * git commit -v
    * git diff --word-diff: show inline word diff
 * git stash
    * stash -p
    * stash -u: include untracked
    * git checkout works from stash, too: git checkout stash@{0} -- <file_path>
 * Config options you should set
    * Merge strategies
    * Pull strategies
    * git config --global branch.autosetuprebase always
    * git config --global help.autocorrect 1: autocorrect typos
 * The Files Forgotten By Git
    * ls-files: -t and --others and --others -i --exclude-standard
    * clean: remove untracked (show with -n)
    * git clean -X -f: remove from gitignore
    * assume-unchanged magic (check-ignore, status --ignored)
 * Fixup commits
    * git commit --fixup <hash>: mark as fix of previous commit
    * git rebase -i --autosquash: squash fixup commits into normal commits
 * Porcelainy
    * git count-objects --human-readable: objects and their disk usage
    * git gc --prune=now --aggressive
 * Use hooks
    * git commit --no-verify
 * Dealing with large repos
    * git clone -b <branch-name> --single-branch https://github.com/user/repo.git
 * Exemplary usage
    * git checkout <deleting_commit>^ -- <file_path>: restore file deleted in commit

 * lessons learned from git manuals
    * there are only 172 of them, better make two parts?

 * libgit2, pygit2 & cool stuff
    * use pygit2 for analysis!
    * use pygit2 for actual interaction

 * git rant: usability, https://git-man-page-generator.lokaltog.net/#


## tools

 * ssh config & tips
    * client: config!
    * server: known_hosts, best practices
    * basics

 * tmux config & tips
    * tiling
    * status line

 * ipython! config & tips
 * vim hacks / lessons learned
 * latex best practices & links
 * pip all the features?
 * überhaupt config, secret vs other config


## kurse

 * machine learning
 * das udacity norvig design ding


## intro
 * django einsteiger
 * ieee754 cheat sheet

## Django+Python

 * DRF
 * py.test
    * ernsthaftes testen: tests im nachhinein in $alles einbauen
 * pybee tools
 * pdb!!

## webstack resources

 * nach level
 * nach lerntyp
