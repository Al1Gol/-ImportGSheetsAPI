import React from 'react'
import axios from 'axios'
import {BrowserRouter, Route, Routes} from 'react-router-dom'

import './App.css';
import OrdersList from './components/OrdersList.js'

class App extends React.Component {
    constructor(props){
        super(props)
        this.socket = new WebSocket('ws://localhost:8000')
        this.request_id = new Date().getTime()
        this.state = {
            'orders': [],
        }
    }

    componentDidMount() {


        this.socket.onopen = (event) => {
            this.socket.send(
                JSON.stringify({
                    action: "list",
                    request_id: this.request_id,
                })
            )
        }
        
        

        this.socket.onmessage = (event) => {
            const orders = JSON.parse(event.data).data
            console.log('Данные:', orders);
            this.setState({
                'orders': orders
            })
        }

        this.socket.onerror = function(error) {
            console.log(`[error] ${error.message}`);
        };
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
