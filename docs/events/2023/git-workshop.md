---
title: Git Workshop (2023)
slug: git-workshop-2023
date_published: 2023-03-26T07:59:45.000Z
date_updated: 2023-03-26T07:59:45.000Z
tags: 
    - Beginner 
    - Getting Started 
    - Workshop
---

This post is based on the workshop that we held on the 22nd of March in-person, it covers everything we covered in the workshop.

This workshop uses the VS Code GUI for interacting with Git, so make sure you have it installed before proceeding.

If you have any questions or issues while following along, feel free to ask in our Discord server!

## What is git?

Git is a “version control” software, which keeps track of code changes and allows multiple people to easily work on the same codebase.

Usually there is a “main/master branch”, where team members branch off to do their work, and then merge their work back into the main/master branch.
![](https://lh6.googleusercontent.com/l08w3ka-Hf0P_NnuxuUmeoTOhGJq7CH-FBKKxKPI4FJaDYDIYxTiukdjGr-oofB_a3jnUAegXnQeBA7RXj1iTSzfHBcdVLCldhrAe57Th8ZuoELBEqVRbJwkvtJWUtru2Yr9tFXFghW7nEgEiP4PDFaS9g=s2048)

This lets both:

- Many people working on the same codebase in parallel without conflicting with each other most of the time
- You alone working on multiple features in parallel, while always being able to undo/discard/roll back your changes

This makes git useful for both large teams as well as personal projects, helping you ensure that no work is ever lost and you can easily keep track of both your and other people's changes.

Basically every company uses git to manage their codebase, with very rare exceptions (e.g. Google developed their own one that basically only they use), but when you enter the industry you're guaranteed to use git at some point.

## GitHub

This guide is centered around GitHub, which is the most popular git hosting service. To clarify the difference using an analogy:

- Git is like a video library, where you can locally manage it, but it's hard to share it
- GitHub is like YouTube, where you could host your video library for everyone to easily see (and comment on), however, YouTube isn't the only place where you can host a video library, with many alternatives like Vimeo and DailyMotion and so on.

Some popular alternatives to GitHub include things like GitLab, BitBucket (Atlassian), Azure Repos (Microsoft), and so on. The companies you join may choose to use another provider instead of GitHub, and you'll have to authenticate with them separately (likely with SSH keys).

Anyway, to follow this guide, make sure you have a GitHub account.

## Installation

Installing and authenticating git is one of the harder parts of getting to know git, and more than half of our workshop time became dedicated to making sure everyone's on the same page with installation.

### Windows

Go to [https://git-scm.com/downloads](https://git-scm.com/downloads) and follow the installation instructions. Make sure you download the "setup" instead of "portable".

When going through the installer, change the following options to make life easier:
![](https://lh4.googleusercontent.com/x6gHqLTgTlWQVlNuQVRhcHa8wJtI46exeHis3DzrpowMRN3OKSY0VBVuF1samfT2d67W-KuMTra3Q8dAfphdx72Iq707YK-rPKBdt5yYuLSZz-iWB3KovkToe-n9qpVhQhNTuVy24m4p15Ssfn_OMlzrnA=s2048)

Most editors in windows these days are happy with Unix-style endings (which are superior anyway), and it's standard to use Unix-style in git. Preventing git from automatically changing endings for you will save you headaches later.

![](https://lh4.googleusercontent.com/k8aQbV2rDZwbz7vl3Sk5uYl-Z94B1EACNdt9WYJXcevLQt6gWIMsiibHLuCn11-KI0mkr3Xq25SZo0RO3vDdcrrqTPhuqKtCfNE6OwMoY8AsWP3jqjqmAttn-pQVhYNTbU_in8U1fLOBvQbea8uEPx5TVw=s2048)

Git sometimes opens an external editor to help resolve some issues, it is very rare but you may as well get it to open VS Code rather than vim.

### MacOS & Linux

Follow the instructions on [https://git-scm.com/downloads](https://git-scm.com/downloads), you may have to install Brew first if you're on Mac.

## Authentication

Authenticating git can be very fiddly. If you're familiar with SSH and SSH keys, here's the official guide to setting it up with GitHub: [https://docs.github.com/en/authentication/connecting-to-github-with-ssh](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

If you're not, then the easiest way is probably using the GitHub CLI.

Install the CLI via: [https://cli.github.com/manual/installation](https://cli.github.com/manual/installation)

If you're on windows, scroll down to "Signed MSI" and go to the releases page, and download `gh_2.25.1_windows_amd64.msi`

### Using GH CLI

After everything's installed, you should be able to open command prompt (cmd.exe) and you'll be able to run both `gh` and `git` without errors.

To authenticate using the gh cli, run: `gh auth login`, then follow the instructions to authenticate:

- **Account:** Github.com
- **Preferred protocol:** HTTPS (Windows), SSH (Mac, Linux)
- **Generate a new key pair (for SSH):** Yes
- **Passphrase (for SSH):** leave it blank and press enter
- **Title (for SSH):** leave it blank and press enter
- **Authenticate:** Log in with browser

Then follow the browser login steps.

After that, you should be logged in.

## Git first-time setup

In order to tell git who you are (for local development), git requires you to run the following commands:

```shell
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

Replace the name and email with your name (or username) and your GitHub email accordingly.

This is a legacy part of Git, however it won't let you make commits until you do it.

## VS Code

Just a reminder that everything below will require VS Code to follow along, so make sure you have it installed from here:

[https://code.visualstudio.com/download](https://code.visualstudio.com/download)

## Beginning a repository

From here, in the workshop, we asked people to form groups of 2+ people and pick a group leader to be the repository owner. If you're alone, it's ok to follow along still, but asking a friend who's learning git alongside you to help would also be fine.

Below are instructions for the group leader to follow:

### Creating the repository

We start by making a new folder for your project and opening that folder in VS Code. Make sure you open the folder in VS Code, rather than just individual files. When you open the terminal (Ctrl+Shift+`) it should show that you're in the correct folder. 

Next, you should copy the files from here:

https://github.com/ProgSoc/git-workshop-project

When clicking a file in GitHub, make sure you click the "Raw" view to see raw content (for the .md file).

![](../../assets/images/workshops/2023-git/image-4.png)

In the end, you should have something like this:

![](../../assets/images/workshops/2023-git/image-5.png)

### Initializing git

Run `git init` in the terminal to initialize the repository, or click "Initialize Repository" in the git tab in VS Code

![](../../assets/images/workshops/2023-git/image-6.png)

The git tab
### Committing the initial files

We will explain what a commit is better further below, but to commit everything, go to the git tab and type in a commit message (probably just "initial commit") and press commit.

### Publish the repository

Press the publish button in the git tab (or type Ctrl+Shift+P and search "publish repository"), then make sure the repository is public (which makes some permission management easier), and follow the prompts if it asks you to log in.

### View your repository

In the bottom right corner, a notification with a button should appear to open the repository, or you can just go to your GitHub account and see it.

### Sharing the repository with other people

If you're working with other people, share the repository with others in the Collaborators tab:

![](https://lh4.googleusercontent.com/ldA5w3HWwMOfYoc4ftB1hTXUzPE0Ve3QKpsRDNhNNHIjoQ5obi1h-H0aGFn2gL3Hby93iDT_7Z0OYzWZmd0b-_v-cXsr-log2qMKOOCqrGxPiJt6hvGTCwpK9Tf-vie6a_1jKauYNIeqqu9vciaoVwaDIA=s2048)

![](https://lh3.googleusercontent.com/V0y4GVRgoKgLPHui7UhGVHIWhT6Fto-EoyDCvsQ2w956WypdAvb3FNjYJ0Q11pFseUAulTmka-LpalTbEoFyisXO7_TH4JfhlLbw8SovE3STYlyXHXCSXBZ39uNB6N_mYVsxqp4IatT73PpMY7hK0AIZJA=s2048)

They should receive an email invitation which, when clicked, would add them to the repository.

### Cloning the repository

`git clone [url]` is a Git command line utility which is used to target an existing repository and create a clone, or copy of the target repository in a local folder.

If you're in a team, other team members you added need to clone it. If you're following along alone, you could clone the repository again in another folder or just ignore this step.

To clone your repository:

1. Open up the terminal
2. Navigate to the folder where you want to store your repository
3. Clone the repository using the either the **HTTPS **or **SSH **URL based on how you authenticated earlier.

![](https://lh5.googleusercontent.com/fRScl0KRkuMudm64EAYB_p9mzhomVP-Y21xBPC4YGuqW-GJKCOm2WsrnQOdimrjfNibx5vwIedeCe8JYeirqsBC-rxWcqQIYpIuNEVvdwqtzh7Q1ifzzHkKTpgocKwyK1Ie4OKOC9Jfno4sJQO4hjvdN3g=s2048)

![](https://lh6.googleusercontent.com/Z3qTn0nTAvHYwWlPsdMPyW3Bu74lTQ87e02km1-Og5VZ2eQEwbI485m9Lrz8jqgLHg_asJjgNTP-qIvctGlLpbE_eVhjd6o6OcxDltUqmZCIwI1fw-xB-9ERpSA8liLA1tGxLveBduWpthbxSisbMwUugQ=s2048)

## Working with your repository

We now have a working repository! Now, we can start making changes to it, just like you would when you're in a real project.

We start by making new branches. In git, branches are a way to maintain a set of changes which are separate from the main codebase. You can make your own branch, make a couple of commits to it, then merge it back into the main codebase (the "master" or the "main" branch).

You and your teammate could have entirely separate branches with different changes, and then you can both merge them into the master branch separately as long as they don't change the same lines (in which case you may get merge conflicts, which we will talk about later).

Multiple people can even merge changes into the same file (again, as long as the exact same lines aren't changed).  

### Creating a new branch

To make a new branch, click the branch button in the bottom left:
![](https://lh4.googleusercontent.com/FMX5AonnuAC1YTz68lDkaFrCaA_1JGqMwfsT0Lz0BrAoXb1-OUTwTNCtgCQJ4B8nkbAFOWCrPpr9QJg0LugwuXmMDVZJv_QmAb0RN8CVBg1IuOcL-viUpmnjD_557IZzN7-XWWdR7N6b-hyXkQxsc5vkBg=s2048)

Then create a new branch:
![](https://lh3.googleusercontent.com/P4lDzWFa3SXuhoPO8II_z7AvAr77UvgbLfVGqSXoYJpUTH3v3jta6ox8giwkw6yeB8dwXrGl5-Q8HMmOiNe_GTPZTH_Dy9Tf4ttjI8YYVfgdmk10FQJr7B8bV-Rtk8WaDQulwh3l7XM5MyE5KY0WE8QLDQ=s2048)

![](https://lh5.googleusercontent.com/p4AzoUTqt1OKQ4568J5czvapM0U16bEk493pe-lwrYsOxrNy4yK5usaSxV9pExo3ekc6l8mipfIxNSS8vDOc6HY9pdMZDjbSTXgN80BiX6MXMB51SpPRabHnpH3juLsD0vXBSJQpV3XrqYk9tRM4m4PEPQ=s2048)

You should then see that you're on the new branch:
![](https://lh3.googleusercontent.com/pXsMAIsvQ90abj8bqSUMq1hgg7OYhkFZ5s7x021-vBgPsPAx5I9Vy2nLtaHvjo_wVRADIA8ivO6nSEaxK1OdmgSbjOQZ-uinichqah7E07Rs1A61Xqz2B-TdAKHvx21-6AZNItMVTbUjz1yFh51FumdsYQ=s2048)

### Making changes to your repository

Now that you have a local copy of your repository, you can start making changes. 

Go ahead and make changes to the README.md or index.js file, and make sure to hit save.
![](https://lh5.googleusercontent.com/q-Z-XcrLoOnEw1UdzYcRdUk-2B_dbcVLJhLKS_lBQ5ml_8MEfUyRSM2Tn7zjViezY0wcOfr_TqR3Sqz2aH1ZJyRKHmofvMJoPtxG9e-tdvQoxqJT145Z56qOLcyb3Ed-D4Zaq75hkpJ1TenGPtrVEgfIag=s2048)
An example "diff", aka a visualisation of the changes I made.
You should see the changes reflected in the git tab of VS Code.

To add your new changes to git staging, add individual files or all changes, by hovering over the changed file and clicking the + icon:
![](https://lh5.googleusercontent.com/6HMUp9cWwMhSQlVi57Jzl_kqLEzs9iqg1xxrKIWJmSjzRtVgKILW6cRJbQ5-FQA6RIcDBEHtYIFm8ENtbcZ-2koaTGkDZj3l_C1ojINMxf5BeVBOlZJ5U50MDjwK7WwVFy8eCMNs6OoL16KeA6loYgBYMA=s2048)

To commit your changes to the git tree, add a commit comment and click commit:
![](https://lh6.googleusercontent.com/SBXQvIPZahMxYhPwof5ncj1LNpeCwFoaLizaro31xTFM3iUJa2Lw_w7BSAqiHwnbZ7CRXdnyu-R42xjEQYjUna6zwT3RMvTJwe-5GL-yOxxrw70ALaXKNsHXtzQRWqmLewJVkXXXBong5Yf67blgxxzxKA=s2048)

### Pushing your changes

When you’ve made a commit, you need to push it to GitHub. If this is a new branch, you need to “Publish” the branch. You can do it by clicking this button:
![](https://lh5.googleusercontent.com/Jr1-wDVtzGU_5Q_kyF1__sKr-PGskfXJU1VE1RDyXj-nbUsOmBawetfQ9O57kAavIsCT7CtAcg4RsCqS9Dw5c62ITqukSNLA0OfcJ0QxpW-UNpayB6KmiuRMjgQ5onnRi_N7ABaCEa82d7DY_sKH0IpNhw=s2048)

After you publish your branch, it should be visible in the list of branches:
![](https://lh6.googleusercontent.com/dWOlGmArw10DhBWIlVf3Ah-pLfS7SolJ7xa7y2xWYHspruC3rCPgJROIoR1PA-zcs6j09s8OBTSq7uwZ1yTm8GVpbJ9n4Vdi-BwvZVZOpR1N168WlsLo9Nezp6IXchyqIhi33nFcsmgUpoxZeRA3U-40sA=s2048)

### Making more commits

We’ve showed you how to publish branches, but you can always make as many commits as you want per branch.

Technically multiple people can commit to the same branch, but it’s not ideal and often leads to merge conflicts.

### Making a pull request

When you are ready to merge your changes into the **master **branch of your repository, you must create a new pull request.

A pull request allows other members of your team to analyse and review the changes you are making to the code, being able to add comments and provide potential improvements.

It is best practice to have your pull request approved by at least one team member before merging the code back into master to mitigate any issues with the code or incorrect changes in functionality.

To create a pull request, you can click this button in GitHub:
![](https://lh4.googleusercontent.com/-Bl37cViajkJ2W1cwHefB1YmYODmqvO7jIoVmr13kPEvH6JbOzK_PMS6GM1gu8VixlgIllbejZFAJ3tvpBMNVZqWwg-3XHo2XaKvRfz3MC2XbN6aAS_xnUQeo-Gag749ZQu9i8bBNgM7bAZS45vvkMR86Q=s2048)

Or click select the branch, then click this:
![](../../assets/images/workshops/2023-git/image-7.png)
Or go to the general branches tab and press "Open pull request" next to the branch.

Next, you can add the pull request information:
![](https://lh6.googleusercontent.com/JA8TB8fzyC8sQ6UKPZbIa9ijRj0x7NlwIwTXcVnI-hHoE0YyN9OpzA5gDRwpotsBYkjAe0L0QrIMZnYyhYCallftGPCBfKHAfLICIR_pLAxeMZCvmJuy4uIR7ecRqYME2ZwcIg5d8TsuPrBNFdYu3bkW4g=s2048)

And then click create!

### Merging a pull request

To merge the changes, press “Merge pull request” and then confirm the merge.

There are multiple types of merges, being merging, squashing, and rebasing.
![](https://lh4.googleusercontent.com/7VYBf-nntvDfKPum-MIEs9koF072d658s0rUGEYQL7BzRxl8incD_smMsN74dDcVn1kARIiamFI4v9PzcFDfxxshyWb0BURw5xmw5VIs9nOwCOAq2E24aYfISJKMq-wmATd7H50ZKVg9mJ1OPBKjkdC2jA=s2048)
![](https://lh4.googleusercontent.com/dNsZgcFy7a1WXqf-vXuu4Py4dZ02U3pB0nKYskxazmIAovu1Ls0ksLHLQ_9_fd3PYWet1kjENW17KdCdma9H25A8NZ1UMl1JQmI8YBT6wGHHx02ETKZO91E5KUXDhTBJjLjok02Rz2TG4774YWF5Ypb5gA=s2048)
![](https://lh6.googleusercontent.com/VZl3QCflAidNQ67iBc2iRAN2QgAsMg6lEsBUCUQgQYJoAsCZzddic2KzPx-S_-r7VSXRoUjEg2RNNbVQMDHbgJu1le9xKLI6gfR1X75ASO4X6PeHMgFvXhWhK4EokS95wTZ_B_8KJy5jGVNV4dWR3SsxnQ=s2048)

The 3 methods of merging are:

- Creating a merge commit: It copies across all of the commits in the branch into the master branch, and then tops it off with a merge commit. This means that each commit you made will be in the master branch's git history.
- Squash and merge: Join all of the commits into 1 big commit, then merge that. This will hide all of the branch's commits, but it looks a bit cleaner in the master branch's git history.
- Rebase and merge: This one is advanced, but basically it replays all commits on top. Explaining this is out of the scope of this post.

### View your changes in the master branch!

Go to the master branch’s commits, and observe that the changes are all now in the master branch.

![](https://lh3.googleusercontent.com/bVdlJxpUu6h1JpY3IFSpb6JDnnCd-mWfpIxn2Fsng0isNtxGkBLq4sqpthbzSJP7GeIOuCChcsJhAMyktHwyXiw-eEqvS6NhYCnwyZtdyVIJ46ohIPMGE53jh0KUuhjD0AN6LdzIzQWUc9cNi576XdLOow=s2048)
![](https://lh5.googleusercontent.com/g-a0fPU5bL3Q_RacomcFHX_h2tG8VvefiGLrQ6qchyuwFB9YHJqadT99A3N7p58B9HqGH6bJjkRXoWOG_ivl_o2l7I9eAXpvsDJij7Tthv-CgjQQgDx--1bFccxAftoHAj9tiH011IkmyGWLvU73sp30Qg=s2048)

As you can see, the PR that was merged leave their commits in the master branch and in the git tree it shows the line connecting back, however squash & merged PR is its own commit and it's disconnected from the branch it belongs to.

Squashing vs just merging is up to personal preference. The workplaces where I've worked prefer squashing, but I know people who prefer merging instead, just make sure your team agrees on one and consistently chooses it.

## Merge conflicts

What happens if multiple people make a change to the same line?

You get a merge conflict!

Merge conflicts show what’s your current change, what’s the incoming change (what you’re trying to merge in), and you have to resolve them.

![](https://lh4.googleusercontent.com/kCAVYvjpR431UmWfhlpyTChViHi7vljNvYOIWxeDmANu3gmRyKVLgjTxiWBg9X0RtReJWsK5m0BX4QU34EDHsTjxFka8yxWWkLgeSfBAShE1qs1bcEub8TMDCcgrLOfrX8B_itj3fx4x1awgFWRCL1wiDg=s2048)

### Inducing a merge conflict

To learn how to deal with merge conflicts, you can force a merge conflict manually for the sake of learning them.

In order to create a merge conflict, do the following:

- From master, 2 people should each create a new branch.
- Both people should make a commit, changing the same line in different ways
- Both people open a pull request
- Merge one of the pull requests
- Observe that now you can’t merge the other pull request
- The other person needs to run `git pull origin master` to update their branch, this shows the merge conflict
- Once it’s resolved, you can push again and the second PR can be merged

If you're doing this alone, you can manually make the 2 different branches and the 2 different pull requests. Just make sure that when you're creating a new branch, you're starting from the master branch.

### Resolving a merge conflict

When you run `git pull origin master` and get a merge conflict, in the git tab of VS Code you'll see the conflicting files. When you click a file, you'll see an interface something like this:

![](https://lh4.googleusercontent.com/kCAVYvjpR431UmWfhlpyTChViHi7vljNvYOIWxeDmANu3gmRyKVLgjTxiWBg9X0RtReJWsK5m0BX4QU34EDHsTjxFka8yxWWkLgeSfBAShE1qs1bcEub8TMDCcgrLOfrX8B_itj3fx4x1awgFWRCL1wiDg=s2048)

"Current" is the branch you're currently on, and "Incoming" is the changes you're merging in, for example, with `git pull origin master`, the "Incoming" changes would be the master branch.

Click the appropriate buttons at the top, and clean up the code, and then you can press the + button next to the file in the git tab, and then you can commit the merge.

After that, you can push again and things should be resolved.

## Gitignore

Creating a .gitignore file in your repository will let you ignore files that you don't want git to track. You can read more about gitignore here:

[Atlassian Gitignore](https://www.atlassian.com/git/tutorials/saving-changes/gitignore)

## Thank you for reading!

This should be the very basics of git, based on the workshop content. If you have any questions, make sure to ask on our Discord server!
