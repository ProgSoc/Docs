---
title: Contributing
description: How to contribute to the ProgSoc Docs
hide:
    - navigation
---

# Contributing

## Making Code Changes

There are different ways you can contribute to ProgSoc Docs:

1. Create an issue on the [GitHub repo](https://github.com/progsoc/docs/issues) with your suggestion
2. Fork the [GitHub repo](https://github.com/progsoc/docs/issues) and make a pull request with your changes
3. Edit the page directly on GitHub and make a pull request with your changes

### Creating an issue

The easiest way, if you're not familiar with Git is to create an issue on the [GitHub repo](https://github.com/progsoc/docs/issues) with any changes you'd like to see. Make sure to include the page you're referring to and the changes you'd like to see. 

If you don't provide enough information we may ask you to make a pull request instead, so that we can see the changes you're suggesting.

### Forking the repo

The best way to contribute to almost any open source project is to fork the repo and make a pull request with your changes. This is the best way to ensure that your changes are accepted and that you're happy with the changes you're suggesting.

If you're not familiar with how Git works make sure to check out our [2022 Git Workshop](./events/2022/git.md). It has all the instructions you need to get started with Git.

1. [Fork the GitHub repo](https://github.com/ProgSoc/Docs/fork) to create your own copy of the repo on GitHub.
2. Make your changes to the files you want to update.
3. Commit your changes to your forked repo.
4. Create a pull request to merge your changes into the main repo, making sure to ask for a review from the ProgSoc committee.
5. Respond to any suggested changes and feedback from the committee.
6. Once your pull request is approved, your changes will be merged into the main repo.

### Editing on GitHub

If you're not familiar with Git, or you just want to make a quick change, you can edit the files directly on GitHub. This is the quickest way to make a change, but it's not the best way to ensure that your changes are accepted.

1. Navigate to the file you want to edit on GitHub.
2. Click the edit button in the top right corner of the file.
3. Make your changes to the file.
4. Commit your changes to your forked repo.
5. Create a pull request to merge your changes into the main repo, making sure to ask for a review from the ProgSoc committee.
6. Respond to any suggested changes and feedback from the committee.

The same button exists at the top right hand corner of any of the existing pages in the docs. If you want to make a change to a page, you can click the edit button and make your changes directly on GitHub.

## Project File Structure and Format

The docs are built using [mkdocs](https://www.mkdocs.org/), a static site generator. The files are written in [markdown](https://www.markdownguide.org/basic-syntax/) and are stored in the `docs` folder. The `mkdocs.yml` file contains the configuration for the site, including the navigation and the theme.

The `docs` folder contains a number of subfolders, each of which contains a number of markdown files. The subfolders are used to group related pages together. For example, the `events` folder contains all the pages related to events, including the [Git](./events/2022/git.md) and [Rust](./events/2022/rust.md) workshops.

Another important folder is the `docs/assets` folder as it contains all the images used in the docs. If you want to add an image to a page, make sure to add it to the `docs/assets` folder first.

> When adding a new page make sure to add it to the `mkdocs.yml` file so that it appears in the navigation.