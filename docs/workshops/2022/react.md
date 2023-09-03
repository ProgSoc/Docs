---
comments: true
---

# React Workshop

## Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/Fr5D1KLGGZc?si=ftjY1ICQRAiGPVxJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## What you’ll learn

- State Management in React
- Typescript with React
- Data fetching
- Virtualisation
- Redux

## Installation and Tool Setup

### NodeJS

#### Mac/Linux

1. Follow the instructions to install the node version manager program.
    
    [GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions](https://github.com/nvm-sh/nvm#installing-and-updating)
    
2. Install the latest LTS version of NodeJS
    
    ```bash
    nvm install --lts
    ```
    
3. Reopen your current terminal

#### Windows

1. Go to https://github.com/coreybutler/nvm-windows/releases and download the latest `.exe` release file
2. If prompted, install and run through the setup process (logout/login)
3. Once installed run this command to install the latest version of NodeJS
    
    <aside>
    🚫 This requires admin
    
    </aside>
    
    ```bash
    nvm install lts
    ```
    

### Yarn

If you’re unfamiliar with how to use a package manager I would recommend installing `Yarn`, an alternative to the built-in Node Package Manager.

1. Install Yarn using NPM
This is quickly done by using the below command:
    
    ```bash
    npm install --global yarn
    ```
    
2. Restart
    - Windows
        
        Log out of your windows account and back in to refresh the programs in your path
        
    - Mac/Linux
        
        Close an reopen a new terminal window to use new paths
        
3. Test to see if it works
    
    ```bash
    yarn --version
    ```
    

### Git

If you’re using `Linux` then it’s likely that GIT is probably already installed. 

On windows and mac you can install it by downloading and installing the executable/app, here.

[Git](https://git-scm.com/)

### Github

If you don’t know what Git is then you can have a quick read of our Intro to Git blog post.

[Introduction to Git](https://progsoc.org/blog/intro-to-git/)

### VSCode

Download and install here:

[Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/)

### Devtools

#### React

[React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi)

#### Redux (Optional)

[Redux DevTools](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd)

## Project Setup

### Project Template

[New Project - Vercel](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fsebasptsch%2Fprogsoc-react-workshop&repository-name=ProgsocReact&project-name=Progsoc+React+Workshop)

### Commands

1. `yarn install` - install dependancies (this might take a minute)
2. `yarn dev` - start the dev server

## TypeScript Intro

[https://www.youtube.com/watch?v=zQnBQ4tB3ZA](https://www.youtube.com/watch?v=zQnBQ4tB3ZA)

## React Libraries and State

[https://www.youtube.com/watch?v=Tn6-PIqc4UM](https://www.youtube.com/watch?v=Tn6-PIqc4UM)

- Explain react component system and how updates propogate using react devtools
- Explain file structure (entrypoints etc. )

### Virtual DOM

- React uses a virtual dom (faster than reading the real DOM) and compares it to the actual dom in order to calculate changes.

### State Updates

React Devtools demo with a basic premade todo app

### Hooks

useState

useEffect, mounting and unmounting

useContext

### React Router

Router setup, defining routes

then after

params in components useParams

## React Todo List

### Setting up a provider

### UI

### Saving state in local storage

### Data Fetching

## Extras

### Virtualisation

[Getting Started with React Virtuoso | React Virtuoso](https://virtuoso.dev/)

[react-window](https://react-window.vercel.app/)

Make sure content that isn’t on the screen isn’t rendered.

### Animation

[Production-Ready Animation Library for React | Framer Motion](https://www.framer.com/motion/)

[react-spring](https://react-spring.dev/)

### State Management

Industry standard state management

[Redux Toolkit | Redux Toolkit](https://redux-toolkit.js.org/)

Simple state management

[React Hooks for Data Fetching - SWR](https://swr.vercel.app/)

### Component Frameworks

[Chakra UI - A simple, modular and accessible component library that gives you the building blocks you need to build your React applications.](https://chakra-ui.com/)

[MUI: The React component library you always wanted](https://mui.com/)

[Primitives - Radix UI](https://www.radix-ui.com/)

[Introduction - Semantic UI React](https://react.semantic-ui.com/)

[React-Bootstrap](https://react-bootstrap.github.io/)

And it goes on and on and on.