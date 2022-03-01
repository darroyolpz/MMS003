# Standard Cost from MMS003

Get standard cost from MMS003 using Qlik Sense. This script is specially useful for getting the cost of several items at once.

## Infor environment

When calling MMS003 query, the figure one should worry about is the standard cost. This is automatically updated and represents the true cost based on the costing model for each division.

![MMS003 from Infor](https://raw.githubusercontent.com/darroyolpz/Std-Cost-MMS003/main/img/MMS003.jpg)

## Data from Qlik Sense

Data retrieved from Qlik Sense has all the pricing updates done for each item. Using the drop_duplicates function help us getting the right cost.

```python
df1 = df.drop_duplicates(subset = 'Item no', keep = 'last')
```

Data then is sent to Excel to perform deeper analysis, massively update pricing lists, store it just in case...you name it.