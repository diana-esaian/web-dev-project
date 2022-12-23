import React, { Component } from 'react';
import './styles.css';

class App extends Component {
  constructor(props) {
      super(props);
      this.state = {
      BackgroundColor: "BLACK"};
  };

render(){
    return (
      <div class='ourbuttons'>
        <button class={this.state.BackgroundColor === "BLACK" ? "Black" : "nothing"}
        onClick={() => {this.setState({BackgroundColor: "WHITE"})}}>CHANGE TO BLACK</button>
        <button class={this.state.BackgroundColor === "WHITE" ? "White" : "nothing"}
        onClick={() => {this.setState({BackgroundColor: "BLACK"})}}>CHANGE TO WHITE</button>
      </div>
    );
  }
}

export default App;
