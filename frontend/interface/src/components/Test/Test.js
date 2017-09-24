import React, { Component } from 'react';
import { Link }  from 'react-router-dom';
import logo from './logo.svg';
import './Test.css';

class Table extends Component{
  render() {
    return (
      <table>
        <tr>
          <td>
            prova
          </td>
            prova
        </tr>
      </table>

    );
  }
}

class Test extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React coglione di merda</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <Table />

      </div>
    );
  }
}

export default Test;
