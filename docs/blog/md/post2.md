# 3 Ways to Create React Components
ReactJS is a great javascript library for reusing HTML code snippets throughout your website. It does so by using JSX and ES6 syntax to infuse your regular Javascript code with pure HTML code and compiles it via Babel to javascript that creates that HTML snippets on the page.
Use CDN to import React and Babel
You can quickly start using React by including the following scripts in your HTML's header tag:
```
<script src="https://unpkg.com/react@15/dist/react.min.js"></script>
<script src="https://unpkg.com/react-dom@15/dist/react-dom.min.js"></script>
```
Additionally, you need to include Babel to compile your React code. Include the following script underneath the others:
```
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.34/browser.js"></script>
```
## Method #1: Using a Variable Function
When React was first created there was only one way to declare a component. Let's build a simple HTML page with an h1 and a p tag.
In your javascript file/tag, declare a variable and use the React.createClass() function to create a component:
```
var MyComponent = React.createClass({
   render() {
      return <div>
                <h1>Hello World!</h1>
                <p>This is my first React Component.</p>
             </div>
      }
})
```

The variable MyComponent now contains a react component that can be used anywhere on a website.
To link that script to an HTML page, first you must have a div element with a unique id on the page.
```<div id="react-component"></div>```
Then in your script after declaring the react component variable, use the ReactDOM.render() function which takes 2 arguments. The first is the react component, and the second is the targeted HTML element.
```ReactDOM.render(<MyComponent />, document.getElementById('react-component'))```
After saving and running the HTML file, the page should display without errors:

Method #2: Using a Class
For those who are not caught up with Javascript evolution news, the language now supports classes. You can create a javascript class the extends (a.k.a. inherits) React's Component class and re-write the above method:
```
class MyComponent extends React.Component{
   render() {
      return <div>
                <h1>Hello World!</h1>
                <p>This is my first React Component.</p>
             </div>
      }
}
```
You would then use ReactDOM.render() the same way again to target the HTML element by id.
## Method #3: Using a Stateless Functional Component
Sounds scary when you say it out loud. But it's really means a simple function (as opposed to a variable) that returns a react component. Here you will see some new ES6 syntax that makes javascript codes shorter and easier to read.
First create a const called MyComponent and set it equal to a function () and use the arrow function => to declare the function logic:
```
const MyComponent = () => {
      return <div>
                <h1>Hello World!</h1>
                <p>This is my first React Component.</p>
             </div>
      }
}
```
Notice that we didn't have to use the render() function inside our function here. We just return the HTML div. It's a nice way to reduce amount of code you write.

And there you have it. These are the 3 main ways you can create a React component! The best way to learn is to write them out and test them in your browser and don't hesitate to read the documentation!