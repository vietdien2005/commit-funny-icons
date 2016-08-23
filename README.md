# commit-funny-icons
Make your commit not bored anymore 
![banner](https://drive.google.com/thumbnail?id=0BxyS1tY8WacOMDB3WkNITTZkT0k&authuser=0&v=1471927057552&sz=w2560-h1406)

## First Step
Crawl icons from http://dongerlist.com/ into folder icons

Command to run: 
```bash
$ python crawl.py
```

## Second Step
Add this line below to your bash profile

```bash
alias randicon="(path_project)/randicon.sh"
```

## Second Three
Change path folder icons in file prepare-commit-msg and copy it to folder your project 

```bash
[path-your-project]/.git/hooks/
```

## Done
Let's try to commit 
