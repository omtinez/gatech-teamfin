# JogRx

JogRx connects your wearable device directly to your Doctor's Electronic Medical System.

## Getting started

Recommend using virtualenv:
```
$ git checkout -b <your-private-branch-name>
$ pip install virtualenv==12.0.7
$ virtualenv env
$ source venv/bin/activate
$ python app.py
```

## Contributing

Make sure you are on your development branch and rebase all changes from master.
```
$ git checkout <your-private-branch-name>
$ git rebase master
```

Push your branch to github
`$ git push origin <your-branch-name>`

Initiate a pull request on github. [Instructions](https://help.github.com/articles/using-pull-requests/) can be found on github

After the pull request is accepted, remove your feature/development branch.
`$ git push <remotename> :<branchname>`


## Database
To create the database locally run `python database/createdb.py` from the project root directory
