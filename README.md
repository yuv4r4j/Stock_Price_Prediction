# Stock_Price_Prediction
Stock_Price_Prediction

### Installation

Clone the repo:

```
git clone https://github.com/yuv4r4j/Stock_Price_Prediction.git
```

Create a branch:
```
git checkout -b <branch-name>
```

 Note: should not commit and push anything to master branch directly without reviewing using 'Pull Request', so create a branch for any repo change, create a pull request for review and merge to master.

Status check:
```
git status
```

Switching to different branches:
```
git checkout <branch-name>
```

Code check-in procedure:
```
1. git add .
2. git commit -m <commit message>
3. git checkout master
4. git pull
5. git checkout <working-branch-name>
6. git merge master # correct the conflicts if any
7. git push -u origin <branch-name> # only for the first push
8. git push origin <branch-name> # for subsequent push
```

### Set up your local machine as a dev environment

1. Install Miniconda (or Anaconda) to help manage your environment.
1. Navigate to the repository's base folder
1. Run the following command to set up (and activate) the `predictive_models` conda environment:

```bash
conda env create -f environment.yml
source activate predictive_models
```

## Authors

* **Chukka Priyanka Reddy** -  [Github](https://github.com/Pri0408)
* **Prabu Manoharan** -  [Github](https://github.com/prabumanohar)
* **Prashanth A** -  [Github](https://github.com/prash2912)
* **Sudhahar Veeramohan** -  [Github](https://github.com/SVAnalytics)
* **Yuvaraj Ganesan** - [Github](https://github.com/yuv4r4j)

See also the list of [contributors](https://github.com/yuv4r4j/Stock_Price_Prediction/graphs/contributors) who participated in this project.

## Acknowledgments/Citations

* Hat tip to anyone whose code was used
* Inspiration
* etc
