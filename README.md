# LeadingAI - Visualising global AI state actors
### Data Visualization (COM-480) - 2024 Project

| Student's name | SCIPER |
|---|---|
| Quentin Esteban | 288211 |
| Malo Ranzetti | 296956 |
| Anne Silvestre de Sacy| 360399|

### [Visit the project homepage](https://leading-ai.mranzetti.com/)

[<img src='https://github.com/com-480-data-visualization/com-480-project-leadingAI/blob/master/milestone-3/rankings.png?raw=true'>](https://leading-ai.mranzetti.com/)

## Project overview

In past years, we have witnessed an unprecedented boom in the A.I sector. Some may think it is a buzzword, others see it as the way forward for society. Regardless, the impact of A.I on our society is undeniable. This project aims to visualize the leading nations in the A.I sector compare to each other. Although strong leaders emerge, we can turn our eyes to the future and imagine who the next important players will be.

This project is based on [Kaggle data](https://www.kaggle.com/datasets/katerynameleshenko/ai-index) by Kateryna Meleshenko, originally provided by [Tortoise Media](https://www.tortoisemedia.com/intelligence/global-ai/).

### [Milestone 1 REPORT (29th March, 5pm)](milestone-1/Data_Visualization_Milestone_1.pdf)

### [Milestone 2 REPORT (26th April, 5pm)](milestone-2/Data_Visualization_Milestone_2.pdf)

## Gallery


[<img src='https://github.com/com-480-data-visualization/com-480-project-leadingAI/blob/master/milestone-3/overview.png?raw=true'>](https://leading-ai.mranzetti.com/)

[<img src='https://github.com/com-480-data-visualization/com-480-project-leadingAI/blob/master/milestone-3/graph2.png?raw=true'>](https://leading-ai.mranzetti.com/)



## Technical overview

This project uses a simple FastAPI backend to serve two webpages as well as a static directory. The frontend is built mainly with D3.js, leaflet.js and vanilla JS. TailwindCSS is used for styling and responsiveness. The project is split into two monolithic pages:
- The homepage, which displays some storytelling and two different graphs.
- The interactive map, which displays the countries and their AI state actors using leaflet.js.

### The homepage
We provide some information about the project and the data. For storytelling, some news headlines are displayed. Using ScrollMagic.js, we trigger different graphs as the user scrolls along the page. The first graph show a bar chart of the scores of the top 15 countries by total score in the index. The second graph is an interactive bubble graph which shows all countries in the dataset. The points are projected by using the total score as the x-axis and the GDP per capita as the y-axis. The size of the bubble is proportional to either the GDP or the Government AI strategy score (depending on the user's choice).

### The interactive map
The interactive map displays the countries and their AI state actors. The user can click on a country to see the score for each of the 7 indicators in the dataset. Clicking on a country will also reveal a density estimation graph for the currently selected indicator, showing the distribution of the scores for all countries.

## How to run the project

To run the project, you need to have Python installed on your machine. 
Then, you can install the requirements by running:
```bash
pip install -r requirements.txt
```

To run the project, you can use the following command:
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

If your machine has make installed, you can also run:
```bash
make requirements
make run
```

