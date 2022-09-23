# **Chocolate Bars Data Analysis overview**



## Data

This database contains over 2,500 chocolate bar ratings from around the globe!

Its focused on plain dark chocolate with an aim of appreciating the flavors of the cacao when made into chocolate. The ratings do not reflect health benefits, social missions, or organic status.

Each chocolate is evaluated from a combination of both objective qualities and subjective interpretation. A rating here only represents an experience with one bar from one batch. Batch numbers, vintages and review dates are included in the database when known.

Flavors of Cacao Rating System:
4.0 - 5.0 = Outstanding
3.5 - 3.9 = Highly Recommended
3.0 - 3.49 = Recommended
2.0 - 2.9 = Disappointing
1.0 - 1.9 = Unpleasant

Note to theingredients column:
B (Beans), S (Sugar), S* (Sweetener other than sugar or beet sugar), C (Cocoa Butter), (V) Vanilla, (L) Lecithin, Sa (Salt)

### **Citations**
- Data information: https://www.kaggle.com/datasets/evangower/chocolate-bar-ratings)


## Exploratory Data Analysis

Utilizing the dataset provided from Kaggle.com I will be answering the following questions starting with my Minimun Viable Product (MVP):

*MVP* 
- What are the top 10 rated chocolate bars?
    - What are the 10 lowest rated chocolate bars?
- What are the top 10 manufactureres by rating?
    - What are the 10 lowest rated?
- Where do the best cocoa beans originate?

*MVP +*
- Does the cocao percentage effect rating?
- Does the number of ingredients effect rating?
- How many different bars did each manufacturer make?
- Is there any relationship at all between rating and other factors?

### *Note:*
*No missing values or outliers were found durring analysis for MVP.*

## **Top and Bottom 10 rated chocolate bars**

### Highest rated Chocolate bars
___
The first question that came up when looking at the data was, "What are the top 10 rated bars?". Through some exploratory analysis it was found that zero bars were rated higher than a 4.0 and there are 112 chocolate bars with a 4.0 rating.

Below is a table, not in any order, of 10 of those 112 high rated chocolate bars along with the review of the flavor highlights.

|            Bar Name           | Rating |    Taste Review (Flavor Notes)   |
|:-----------------------------:|:------:|:--------------------------------:|
| Piura, Choc. Garage Exclusive |   4.0  | creamy, cocoa, grapes            |
| Bejofo, 2019 H., Batch 20     |   4.0  | cherry, perfectly balanced roast |
| Tumaco                        |   4.0  | smooth, nutty, cocoa             |
| Manjari                       |   4.0  | creamy, blueberry, raspberry     |
| Asante                        |   4.0  | simple, delicate cocoa, long     |
| Chuao, batch 1089             |   4.0  | mild strawberry, cocoa, acidic   |
| Valle de Los Rios, batch 990  |   4.0  | complex, strawberry, floral      |
| San Juan de Cheni             |   4.0  | banana, pear, spice, cheese      |
| Maya Mtn, Batch 454, Heirloom |   4.0  | bright fruit, molasses, nutty    |
| Haiti                         |   4.0  | nuts, butterscotch, brownie      |
___
### Lowest rated Chocolate bars
___
Naturally, having found the highest rated, "What are the lowest rated bars?" was the next question. Looking at the data, 50 bars were rated at a 2.0 or lower. 


The following graph depicts the 10 lowest ranking bars.

![](../Mid-Term-Project/images/Lowest%20Rated%20Chocolate%20Bar.png)

Below is a table with the lowest rated bars and thier review.

|            Bar Name           |     Taste Review (Flavor Notes)    |
|:-----------------------------:|:----------------------------------:|
|       Sensations Intense      |        this is not chocolate       |
| Principe, Sao Tome & Principe |     chalky, musty, very bitter     |
|              Dark             |      pastey, strong off flavor     |
|             Baking            |            bitter, cocoa           |
|           Houseblend          |         chemical, salt, wtf        |
|       Ecuador Puristique      |        high intensity bitter       |
|          100 percent          |    sticky, intense, very bitter    |
|           Pichincha           | klingy, hint of fruit, very bitter |
|    El Oro, Hacienda de Oro    |   cardboard, very bitter, floral   |
|             Ghana             |      perfume, strong chemical      |

___

## **Highest and Lowest Rated Manufacturer**
___
After looking at the highest and lowest ranked bars I wanted to look at which manufacturers had the highest and lowest ratings. The following graph shows the 10 highest and 10 lowest rated (cumulative) manufacturers.

![](../Mid-Term-Project/images/Manufacturererating.png)

___
## Highest/Lowest rated bean origins
___

After looking at the best rated chocolate bars and the best manufacturers the question was raised, "Where do the best beans
originate?". the following graph shows the cumulative ratings of each bean origin.

![](../Mid-Term-Project/images/BeanOriginrating.png)


