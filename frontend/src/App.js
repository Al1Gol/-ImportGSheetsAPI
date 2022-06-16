import React from 'react'
import axios from 'axios'
import {BrowserRouter, Route, Routes, Navigate, useLocation, Link} from 'react-router-dom'

import './App.css';
import OrdersList from './components/OrdersList.js'

class App extends React.Component {
    constructor(props){
        super(props)
        this.state = {
            'orders': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/orders/')
            .then(response => {
                const orders = response.data
                this.setState({
                    'orders': orders
                })
                this.state.orders = orders
            })
            .catch(error => {
                this.setState({
                    'users': []
                })
                console.log(error)
            })
    }
     
    render(){  
        return (  
            <div className='container'>
                <BrowserRouter>
                    <Routes>
                        <Route exact path='/' element = {<OrdersList orders={this.state.orders}/>} />
                    </Routes>
                </BrowserRouter>
            </div>
        )  
    }
}
  



export default App;
