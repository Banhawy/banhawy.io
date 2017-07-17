var AgileCircle = Circles.create({
  id:                  'circles-1',
  radius:              60,
  value:               100,
  maxValue:            100,
  width:               10,
  text:                function(){return '<h4>Agile<h4>';},
  colors:              ['#97d5ec', '#028cd5'],
  duration:            400,
  wrpClass:            'circles-wrp',
  textClass:           'circles-text',
  valueStrokeClass:    'circles-valueStroke',
  maxValueStrokeClass: 'circles-maxValueStroke',
  styleWrapper:        true,
  styleText:           true
});

var FontEndCircle = Circles.create({
  id:                  'circles-2',
  radius:              60,
  value:               98,
  maxValue:            100,
  width:               10,
  text:                function(){return '<h4>Front-End<h4>';},
  colors:              ['#97d5ec', '#028cd5'],
  duration:            400,
  wrpClass:            'circles-wrp',
  textClass:           'circles-text',
  valueStrokeClass:    'circles-valueStroke',
  maxValueStrokeClass: 'circles-maxValueStroke',
  styleWrapper:        true,
  styleText:           true
});

var BackEndCircle = Circles.create({
  id:                  'circles-3',
  radius:              60,
  value:               50,
  maxValue:            100,
  width:               10,
  text:                function(){return '<h4>Back-End<h4>';},
  colors:              ['#97d5ec', '#028cd5'],
  duration:            400,
  wrpClass:            'circles-wrp',
  textClass:           'circles-text',
  valueStrokeClass:    'circles-valueStroke',
  maxValueStrokeClass: 'circles-maxValueStroke',
  styleWrapper:        true,
  styleText:           true
});

/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = "white";
}
