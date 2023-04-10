from django.shortcuts import render
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from django_pandas.io import read_frame
from doctor.models import storedatamodel


def decision(request):

    qs = storedatamodel.objects.all()
    data = read_frame(qs)
    data = data.fillna(data.mean())
    #data[0:label]
    data.info()
    print(data.head())
    print(data.describe())
    #print("data-label:",data.label)
    dataset = data.iloc[:,[6,7]].values
    print("x",dataset)
    dataset1 = data.iloc[:,-1].values
    print("y",dataset1)
    print("shape",dataset.shape)
    X = dataset
    y = dataset1
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3,random_state=0)

    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier()

    # Train Decision Tree Classifer
    clf = clf.fit(X_train,y_train)
    
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)

    m = confusion_matrix(y_test, y_pred)
    accurancy = classification_report(y_test, y_pred)
    
    print(accurancy)
    print(m)
    x = accurancy.split()
    print("Toctal splits: ", len(x))
    dict = {

        "m": m,
        "accurancy": accurancy,
        'len0': x[0],
        'len1': x[1],
        'len2': x[2],
        'len3': x[3],
        'len4': x[4],
        'len5': x[5],
        'len6': x[6],
        'len7': x[7],
        'len8': x[8],
        'len9': x[9],
        'len10': x[10],
        'len11': x[11],
        'len12': x[12],
        'len13': x[13],
        'len14': x[14],
        'len15': x[15],
        'len16': x[16],
        'len17': x[17],
        'len18': x[18],
        'len19': x[19],
        'len20': x[20],
        'len21': x[21],
        'len22': x[22],
        'len23': x[23],
        'len24': x[24],
        'len25': x[25],
        'len26': x[26],
        'len27': x[27],
        'len28': x[28],
        # 'len29': x[29],
        # 'len30': x[30],
        # 'len31': x[31],
        # 'len32': x[32],
        # 'len33': x[33],



    }
    return render(request, 'admin/navieaccuracy.html', dict)