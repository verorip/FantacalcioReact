import React from 'react';
import ReactDOM from 'react-dom';
import {BrowserRouter, Route} from 'react-router-dom';
import './index.css';
import App from './components/App/App';
import Test from './components/Test/Test'
import registerServiceWorker from './registerServiceWorker';




ReactDOM.render(
                <BrowserRouter>
                  <div>
                    <Route exact path="/" component={App} />
                    <Route exact path="/admin" component={Test} />
                  </div>
                  </BrowserRouter>, document.getElementById('root'));
registerServiceWorker();
