def analyze_crops(plot1, plot2, plot3):
    all_crops = {'картофель', 'укроп', 'морковь', 'горох', 'капуста', 'редис'}
    common_crops = plot1 & plot2 & plot3
    any_crops = plot1 | plot2 | plot3
    missing_crops = all_crops - any_crops
    return common_crops, any_crops, missing_crops

plot1 = {'картофель', 'укроп', 'морковь'}
plot2 = {'картофель', 'горох', 'капуста'}
plot3 = {'картофель', 'редис', 'морковь'}

common, any_crops, missing = analyze_crops(plot1, plot2, plot3)
print(f"Культуры на каждом участке: {common}")
print(f"Культуры хотя бы на одном участке: {any_crops}")
print(f"Культуры, которых нет ни на одном участке: {missing}")