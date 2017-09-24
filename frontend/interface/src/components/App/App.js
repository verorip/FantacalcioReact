import React, { Component } from 'react';
import { Link }  from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
document.body.style.backgroundColor = "#b3e6ff";


class Table extends Component{
  componentDidMount(){
    var myTable =document.getElementsByClassName('App-table');
    alert(this.refs.chart.rows[2].length);
    var newTable = document.createElement('table');
    var maxColumns = 0;
    // Find the max number of columns
    for(var r = 0; r < this.refs.chart.rows[0].cells.length; r++) {
        if(this.refs.chart.rows[r].cells.length > maxColumns) {
            maxColumns = this.refs.chart.rows[r].cells.length;
        }
    }


    for(var c = 0; c < maxColumns; c++) {
        newTable.insertRow(c);
        for(var r = 0; r < this.refs.chart.rows[0].cells.length; r++) {
            if(this.refs.chart.rows[r].cells.length <= c) {
                newTable.rows[c].insertCell(r);
                newTable.rows[c].cells[r] = '-';
            }
            else {
                newTable.rows[c].insertCell(r);
            newTable.rows[c].cells[r].innerHTML = this.refs.chart.rows[0].cells[c].innerHTML;
            }
        }
    }
    /*var div = document.getElementById('Table-container');*/
    newTable.classList.add('App-Table');
    this.refs.tblcnt.appendChild(newTable);
  }

  render() {
    return (
      <div ref="tblcnt" className="Table-container">
        <table ref="chart" className="App-table">
          <tr>
            <th>
              Bassi
            </th>
            <th>
              Giocatore B
            </th>
            <th>
              Giocatore C
            </th>
            <th>
              Giocatore C
            </th>
          </tr>
          <tr>
            <th>
              Fabio
            </th>
            <th>
              Giocatore B
            </th>
            <th>
              Giocatore C
            </th>
            <th>
              Giocatore C
            </th>
          </tr>
          <tr>
            <th>
              Boss
            </th>
            <th>
              Giocatore B
            </th>
            <th>
              Giocatore C
            </th>
            <th>
              Giocatore C
            </th>
          </tr>
        </table>
      </div>
    );
  }
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Fantacalcio</h2>
        </div>
        <p className="App-intro">
          <img src={logo} className="App-logo" alt="logo" />
        </p>
        <Table />
      </div>
    );
  }
}

export default App;
