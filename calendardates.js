var YEAR = 2019

var FULL_MONTH_NAMES = {
    1  : 'January',
    2  : 'Feburary',
    3  : 'March',
    4  : 'April',
    5  : 'May',
    6  : 'June',
    7  : 'July',
    8  : 'August',
    9  : 'September',
    10 : 'October',
    11 : 'November',
    12 : 'December'
}

var MOTNH_NUMBERS = {
    1  :'Jan',
    2  :'Feb',
    3  :'Mar',
    4  :'Apr',
    5  :'May',
    6  :'June',
    7  :'July',
    8  :'Aug' ,
    9  :'Sept',
    10 :'Oct',
    11 :'Nov',
    12 :'Dec' 
}
var MONTH_KEY_VALUES = {
    'Jan' : 1,
    'Feb' : 4,
    'Mar' : 4,
    'Apr' : 0,
    'May' : 2,
    'June': 5,
    'July': 0,
    'Aug' : 3,
    'Sept': 6,
    'Oct' : 1,
    'Nov' : 4,
    'Dec' : 6
}
var monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


function getFullMonthName(monthNumber)  {
    return FULL_MONTH_NAMES[monthNumber];
}


function createDays(numDays)  {
    tdList = []
    for (var i = 1; i < numDays + 1; i++) {
        var td = document.createElement('td');
        var button = document.createElement('button');
        button.setAttribute('class', 'btn btn-primary');
        button.setAttribute('data-toggle', 'modal');
        button.setAttribute('data-target', '#exampleModal');
        button.setAttribute('onclick', 'setUpModal(' + i  +')');
        $(button).html(i);
        td.appendChild(button);
        tdList.push(td)
    }
    return tdList;
}

function findStartingDay (month)  {
    monthName = MOTNH_NUMBERS[month];
    // Get last two digits
    calculation = Math.floor((YEAR  % 100) / 4);
    // Add the day of the month
    calculation = calculation + 1;
    // Add months key value
    calculation = calculation + MONTH_KEY_VALUES[monthName];
    // Add century code
    calculation = calculation + 6;
    // Add last to digit of the year
    calculation = calculation + (YEAR  % 100);
    // Mod by 7 two get the day of the week.
    calculation = calculation % 7;
    return calculation;
}

function createMonth (monthNumber)  {
    rows = []
    
    startingDay = findStartingDay(monthNumber) - 1;
    var days = createDays(monthDays[monthNumber-1]);

    var tr = document.createElement('tr');
    for (var i = 1; i < startingDay + 1; i++)  {
        var td = document.createElement('td');
        var button = document.createElement('button');
        button.setAttribute('hidden', 'true');
        button.setAttribute('class', 'btn btn-secondary');
        button.setAttribute('data-toggle', 'modal');
        button.setAttribute('data-target', '#exampleModal');
        $(button).html('X');
        td.appendChild(button);
        tr.appendChild(td);
    }
    console.log(days.length)
    for (var i = startingDay, j = 0; j < days.length; i++, j++) {
        if (i % 7 == 0)  {
           rows.push(tr);
           var tr = document.createElement('tr');
        }
        tr.appendChild(days[j]);
    }
    rows.push(tr);
    return rows;
}


function createRow(startingDay)  {
    var tr = document.createElement('tr');
    for (var i = startingDay ; i < 7 + startingDay; i++)  {
        
        tr.appendChild(td)
    }
    return tr;   
}




function alertTest()  {
    alert("im here from calendardates.js")
}