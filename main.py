import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import seaborn as sb
import pingouin as pg
from scipy.stats import kstest
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

iris = load_iris()


# датафрейм имеет вид таблицы со столбами: 'sepal length (cm)' , 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'
iris_pd = pd.DataFrame(data=np.c_[iris['data']], columns=iris['feature_names'])
undepend = np.array(iris_pd['petal length (cm)']).reshape((-1, 1))
depended = (iris_pd['sepal length (cm)'], iris_pd['sepal width (cm)'], iris_pd['petal width (cm)'])


def box_plots():
    for caharateristic in iris_pd:
        print(iris_pd[caharateristic].describe(), end='\n*****************\n')
    sb.boxplot(data=iris_pd)
    plt.show()


# .corr()-метод для парных коэфов
def heat_map():
    sb.heatmap(data=iris_pd.corr(), annot=True, cmap='coolwarm', linewidths=3, linecolor='black')
    plt.show()


def heat_map_p():
    sb.heatmap(data=iris_pd.pcorr(), annot=True, cmap='coolwarm', linewidths=3, linecolor='black')
    plt.show()


def partial_heat():
    dat = pg.pcorr(iris_pd)
    sb.heatmap(data=dat, annot=True, cmap='coolwarm', linewidths=3, linecolor='black')
    plt.show()


# H0- норм распределение alpha = 0.05
def kolmogorov_check():
    for i in iris_pd:
        print(i, kstest(iris_pd[i], 'norm'), sep='\n')


def histograms():
    plt.subplot(2, 2, 1)
    plt.hist(iris_pd['sepal length (cm)'], bins=20)
    plt.title('Длина Чашелистика')
    plt.subplot(2, 2, 2)
    plt.hist(iris_pd['sepal width (cm)'], bins=20)
    plt.title('Ширина Чашелистика')
    plt.subplot(2, 2, 3)
    plt.hist(iris_pd['petal length (cm)'], bins=20)
    plt.title('Длина Лепестка')
    plt.subplot(2, 2, 4)
    plt.hist(iris_pd['petal width (cm)'], bins=20)
    plt.title('Ширина лепестка')
    plt.show()


def qqplots():
    pg.qqplot(iris_pd['sepal length (cm)'])
    plt.title('sepal length (cm)')
    pg.qqplot(iris_pd['sepal width (cm)'])
    plt.title('sepal width (cm)')
    pg.qqplot(iris_pd['petal length (cm)'])
    plt.title('petal length (cm)')
    pg.qqplot(iris_pd['petal width (cm)'])
    plt.title('petal width (cm)')
    plt.show()


def scat_plot():
    plt.subplot(2, 2, 1)
    plt.scatter(iris_pd['petal length (cm)'], iris_pd['sepal length (cm)'])
    plt.title('petal length(x) - sepal length')
    plt.subplot(2, 2, 2)
    plt.scatter(iris_pd['petal length (cm)'], iris_pd['sepal width (cm)'])
    plt.title('petal length(x) - sepal width')
    plt.subplot(2, 2, 3)
    plt.scatter(iris_pd['petal length (cm)'], iris_pd['petal width (cm)'])
    plt.title('petal length(x) - petal width')
    plt.show()


def threed_scatter():
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(projection='3d')
    sequence_containing_x_vals = iris_pd['petal length (cm)']
    sequence_containing_y_vals = iris_pd['sepal length (cm)']
    sequence_containing_z_vals = iris_pd['petal width (cm)']
    ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
    plt.show()


def par_regr_petlen_seplen():
    model = LinearRegression().fit(undepend, depended[0])
    r_sq = model.score(undepend, depended[0])
    print('Анализпарной регрессии между длиной лепестка и длиной чашелистика')
    print('coef determination', r_sq)
    print('b0 coef:',model.intercept_)
    print('k coef:', model.coef_, end='\n******************\n')
    plt.scatter(iris_pd['petal length (cm)'], iris_pd['sepal length (cm)'])
    plt.plot(iris_pd['petal length (cm)'], model.predict(undepend), color='Red')
    plt.title('petal length(x) - sepal length')
    plt.show()


def par_regr_petlen_sepwid():
    model = LinearRegression().fit(undepend, depended[1])
    r_sq = model.score(undepend, depended[1])
    print('Анализпарной регрессии между длиной лепестка и шириной чашелистика')
    print('coef determination', r_sq)
    print('b0 coef:',model.intercept_)
    print('k coef:', model.coef_, end='\n******************\n')
    plt.scatter(iris_pd['petal length (cm)'], iris_pd['sepal width (cm)'])
    plt.plot(iris_pd['petal length (cm)'], model.predict(undepend), color='Red')
    plt.title('petal length(x) - sepal width')
    plt.show()
    prediction = model.predict(undepend)
    print(f'MAE = {(1 / 150) * sum([abs(iris_pd["petal length (cm)"][i] - prediction[i]) for i in range(len(prediction))])}')


def par_regr_petlen_petwid():
    model = LinearRegression().fit(undepend, depended[2])
    r_sq = model.score(undepend, depended[2])
    print('Анализпарной регрессии между длиной лепестка и шириной лепестка')
    print('coef determination', r_sq)
    print('b0 coef:',model.intercept_)
    print('k coef:', model.coef_, end='\n******************\n')
    plt.scatter(iris_pd['petal length (cm)'], iris_pd['petal width (cm)'])
    plt.plot(iris_pd['petal length (cm)'], model.predict(undepend), color='Red')
    plt.title('petal length(x) - petal width')
    plt.show()
    prediction = model.predict(undepend)
    print(f'MAE = {(1/150)*sum([abs(iris_pd["petal length (cm)"][i] - prediction[i]) for i in range(len(prediction))])}')


def ost_regr_petlen_seplen():
    model = LinearRegression().fit(undepend, depended[0])
    predskazanie = model.predict(undepend)
    ls = [float(depended[0][i] - predskazanie[i]) for i in range(len(predskazanie))]
    fig = plt.figure(figsize=(12,10))
    fig = fig.add_subplot()
    fig.grid()
    plt.scatter(undepend,ls)
    plt.plot(undepend, [0]*150, color='Red')
    plt.title('Остатки от длины чашелистика')
    pg.qqplot(ls)
    plt.show()


def ost_regr_petlen_petwid():
    model = LinearRegression().fit(undepend, depended[2])
    predskazanie = model.predict(undepend)
    ls = [float(depended[2][i] - predskazanie[i]) for i in range(len(predskazanie))]
    fig = plt.figure(figsize=(12, 10))
    fig = fig.add_subplot()
    fig.grid()
    plt.scatter(undepend, ls)
    plt.plot(undepend, [0] * 150, color='Red')
    plt.title('Остатки от ширины лепестка')
    pg.qqplot(ls)
    plt.show()


def ost_regr_petlen_sepwid():
    model = LinearRegression().fit(undepend, depended[1])
    predskazanie = model.predict(undepend)
    ls = [float(depended[1][i] - predskazanie[i]) for i in range(len(predskazanie))]
    fig = plt.figure(figsize=(8, 6))
    fig = fig.add_subplot()
    fig.grid()
    plt.scatter(undepend, ls)
    plt.plot(undepend, [0] * 150, color='Red')
    plt.title('Остатки от ширины чашелистика')
    pg.qqplot(ls)
    plt.show()


def mozh_regr():
    X = iris_pd.drop(columns=['petal length (cm)', 'sepal width (cm)'])
    y = iris_pd['petal length (cm)']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)
    coef_df = pd.DataFrame(model.coef_, X.columns, columns=['Coeffs'])
    print(coef_df)
    print(f'intercept {model.intercept_}')
    print(f'coef determination {model.score(X, y)}')
    det = model.score(X, y)
    print(f'mulipile corr coef {model.score(X, y) ** 0.5}')
    print(f'Скорректированный кф детерминации {1 - (1 - det)*(149 / (150 - 2 - 1))}')
    y_pred = model.predict(X_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    reg_m = LinearRegression().fit(iris_pd.drop(columns=['petal length (cm)', 'sepal width (cm)']), iris_pd['petal length (cm)'])
    prediction = reg_m.predict(iris_pd.drop(columns=['petal length (cm)', 'sepal width (cm)']))
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('predicted_pet_len')
    ax.set_ylabel('sepal length (cm)')
    ax.set_zlabel('petal width (cm)')
    sequence_containing_x_vals = prediction
    sequence_containing_y_vals = iris_pd['sepal length (cm)']
    sequence_containing_z_vals = iris_pd['petal width (cm)']
    ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
    plt.show()
    y = []
    for i in range(len(prediction)):
        y.append(model.intercept_ + 0.5598*iris_pd['sepal length (cm)'][i] + 1.7772*iris_pd['petal width (cm)'][i])
    y.sort()
    real = sorted(iris_pd['petal length (cm)'])
    ls = [(real[i] - y[i]) for i in range(len(prediction))]
    plt.scatter(iris_pd['petal length (cm)'], ls)
    plt.plot(undepend, [0] * 150, color='Red')
    plt.title('График остатков')
    plt.show()
    pg.qqplot(ls)
    plt.show()
    print(f'MAE = {(1/150)*sum([abs(iris_pd["petal length (cm)"][i] - prediction[i]) for i in range(len(prediction))])}')
par_regr_petlen_sepwid()