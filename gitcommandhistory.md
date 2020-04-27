
shash@LAPTOP-7LICHIO1 MINGW64 ~
$ git --version
git version 2.26.2.windows.1

shash@LAPTOP-7LICHIO1 MINGW64 ~
$ git config --global user.name "Shashender Kumar"

shash@LAPTOP-7LICHIO1 MINGW64 ~
$ git config --global user.email "shashender@gmail.com"

shash@LAPTOP-7LICHIO1 MINGW64 ~
$ cd Desktop

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop
$ mkdir 2020-04-27-git-shash

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop
$ cd 2020-04-27-git-shash

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash
$ ls

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash
$ ls -a
./  ../

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash
$ git init
Initialized empty Git repository in C:/Users/shash/Desktop/2020-04-27-git-shash/.git/

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls -a
./  ../  .git/

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ notepad++ readme.txt
bash: notepad++: command not found

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git config --global core.editor "nano -w
> "

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ nano readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ nano readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls
readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        readme.md

nothing added to commit but untracked files present (use "git add" to track)

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git add readme.md
warning: LF will be replaced by CRLF in readme.md.
The file will have its original line endings in your working directory

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git commit
Aborting commit due to empty commit message.

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git rm --cached readme.md
rm 'readme.md'

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls
readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls -lrt
total 1
-rw-r--r-- 1 shash 197609 86 Apr 27 20:34 readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        readme.md

nothing added to commit but untracked files present (use "git add" to track)

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ nano readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        readme.md

nothing added to commit but untracked files present (use "git add" to track)

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git add readme.md
warning: LF will be replaced by CRLF in readme.md.
The file will have its original line endings in your working directory

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git commit
Aborting commit due to empty commit message.

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ^C

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git log
fatal: your current branch 'master' does not have any commits yet

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ history
    1  exit
    2  quit
    3  exit
    4  git --version
    5  git config --global user.name "Shashender Kumar"
    6  git config --global user.email "shashender@gmail.com"
    7  cd Desktop
    8  mkdir 2020-04-27-git-shash
    9  cd 2020-04-27-git-shash
   10  ls
   11  ls -a
   12  git init
   13  ls -a
   14  git status
   15  notepad++ readme.txt
   16  git config --global core.editor "nano -w
"
   17  nano readme.md
   18  ls
   19  nano readme.md
   20  ls
   21  git status
   22  git add readme.md
   23  git status
   24  git commit
   25  git status
   26  git rm --cached readme.md
   27  ls
   28  ls -lrt
   29  git status
   30  nano readme.md
   31  git status
   32  git add readme.md
   33  git status
   34  git commit
   35  git log
   36  history

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ nano readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git add readme.md
warning: LF will be replaced by CRLF in readme.md.
The file will have its original line endings in your working directory

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git rm --cached readme.md
rm 'readme.md'

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        readme.md

nothing added to commit but untracked files present (use "git add" to track)

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git add readme.md
warning: LF will be replaced by CRLF in readme.md.
The file will have its original line endings in your working directory

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git commit
Aborting commit due to empty commit message.

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git rm -cached readme.md
error: did you mean `--cached` (with two dashes)?

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git rm --cached readme.md
rm 'readme.md'

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        readme.md

nothing added to commit but untracked files present (use "git add" to track)

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git add readme.md
warning: LF will be replaced by CRLF in readme.md.
The file will have its original line endings in your working directory

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls
readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ nano readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git nano readme.md
git: 'nano' is not a git command. See 'git --help'.

The most similar commands are
        annotate
        daemon

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ nano readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls
readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git rm --cached readme.md
rm 'readme.md'

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls
readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        readme.md

nothing added to commit but untracked files present (use "git add" to track)

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git add readme.md
warning: LF will be replaced by CRLF in readme.md.
The file will have its original line endings in your working directory

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ^C

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ cat readme.md
-init this will create a repository
-ls this will list the content of the directory

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ nano readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ cat readme.md
-init: this will create a repository
-ls: this will list the content of the directory

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ cat README.md
-init: this will create a repository
-ls: this will list the content of the directory

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git rm --cached readme.md
error: the following file has staged content different from both the
file and the HEAD:
    readme.md
(use -f to force removal)

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git rm --cached readme.md
error: the following file has staged content different from both the
file and the HEAD:
    readme.md
(use -f to force removal)

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git add README.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   readme.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git commit -m 'Initial commit'
[master (root-commit) f7fd2d7] Initial commit
 1 file changed, 2 insertions(+)
 create mode 100644 readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls
readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ nano README.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git add README.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git commit -m 'First 2nd commit'
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git log
commit f7fd2d717f17a1be615ec07b73c9ad4f2ae9e7bc (HEAD -> master)
Author: Shashender Kumar <shashender@gmail.com>
Date:   Mon Apr 27 21:44:04 2020 +0530

    Initial commit

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ nano .gitignore

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls
readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls -a
./  ../  .git/  .gitignore  readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git remote add origin https://github.com/shashenderkumar/2020-04-27-git-shash.git

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git remote -v
origin  https://github.com/shashenderkumar/2020-04-27-git-shash.git (fetch)
origin  https://github.com/shashenderkumar/2020-04-27-git-shash.git (push)

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git push origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 280 bytes | 40.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/shashenderkumar/2020-04-27-git-shash.git
 * [new branch]      master -> master

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ nano README.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git add README.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git commit -m 'First 3rd commit after setup'
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git push origin master
Everything up-to-date

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git add .gitignore
warning: LF will be replaced by CRLF in .gitignore.
The file will have its original line endings in your working directory

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md


shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git commit -u 'commit git ignore'
error: pathspec 'commit git ignore' did not match any file(s) known to git

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git commit -u "commit git ignore"
error: pathspec 'commit git ignore' did not match any file(s) known to git

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git commit -m "commit git ignore"
[master 2bb3c0b] commit git ignore
 1 file changed, 1 insertion(+)
 create mode 100644 .gitignore

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git push origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 287 bytes | 143.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/shashenderkumar/2020-04-27-git-shash.git
   f7fd2d7..2bb3c0b  master -> master

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ cat README.md
-init: this will create a repository
-ls: this will list the content of the directory
-status: keeps track of the current work
-remote: a place where the git repository is stored e.g. GitHub

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git add README.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git commit -m "readme append"
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git push origin master
Everything up-to-date

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git commit -a
warning: LF will be replaced by CRLF in readme.md.
The file will have its original line endings in your working directory
Aborting commit due to empty commit message.

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls
readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ cat readme.md
-init: this will create a repository
-ls: this will list the content of the directory
-status: keeps track of the current work
-remote: a place where the git repository is stored e.g. GitHub

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ^C

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git pull origin master
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 812 bytes | 2.00 KiB/s, done.
From https://github.com/shashenderkumar/2020-04-27-git-shash
 * branch            master     -> FETCH_HEAD
   2bb3c0b..c83d441  master     -> origin/master
error: Your local changes to the following files would be overwritten by merge:
        readme.md
Please commit your changes or stash them before you merge.
Aborting
Updating 2bb3c0b..c83d441

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git restore readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
nothing to commit, working tree clean

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git pull origin master
From https://github.com/shashenderkumar/2020-04-27-git-shash
 * branch            master     -> FETCH_HEAD
Updating 2bb3c0b..c83d441
Fast-forward
 readme.md | 4 ++++
 1 file changed, 4 insertions(+)

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ cat readme.md
-init this will create a repository
-ls this will list the content of the directory
-status: keeps track of the current work
-remote: a place where the git repository is stored e.g. GitHub
-push: push from git to github
-pull: pull from github to git

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
nothing to commit, working tree clean

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git status
On branch master
nothing to commit, working tree clean

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls
readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ git pull origin master
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 1023 bytes | 2.00 KiB/s, done.
From https://github.com/shashenderkumar/2020-04-27-git-shash
 * branch            master     -> FETCH_HEAD
   c83d441..84c50e8  master     -> origin/master
Updating c83d441..84c50e8
Fast-forward
 history.md | 35 +++++++++++++++++++++++++++++++++++
 1 file changed, 35 insertions(+)
 create mode 100644 history.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$ ls
history.md  readme.md

shash@LAPTOP-7LICHIO1 MINGW64 ~/Desktop/2020-04-27-git-shash (master)
$
