import "./login-register-box.styles.css"
import { LabelAndInput } from "../label-and-input/label-and-input.component.jsx"
import React from "react";
import axios from 'axios';
import {Redirect} from 'react-router-dom';

class LoginRegisterBox extends React.Component {
    constructor(props) {
        super(props);

        this.state = { login: '', password: '', redirect: false};
    }

    handleSubmit = event => {
        event.preventDefault();
        
        axios.post(`http://127.0.0.1:8000/api-token/`, { username: this.state.login, password: this.state.password })
        .then(res => {
            if (res.status === 200) {
                this.setState({redirect: true})
            }
        })

    }

    handleLoginChange = event => {
        this.setState({ login: event.target.value });
    }

    handlePasswordChange = event => {
        this.setState({ password: event.target.value });
    }

    render() {
        const redirect = this.state.redirect;

        if (redirect){
            return <Redirect to='/choose'/>
        }

        return (
            <form className="outer-box" onSubmit={this.handleSubmit}>
                <div className="inner-box">
                    <LabelAndInput className="login" label="login" value={this.state.value} onChange={this.handleLoginChange} />
                    <LabelAndInput className="password" label="password" value={this.state.value} onChange={this.handlePasswordChange} />
                </div>
                <p className="register">register</p>
                <button type="submit"></button>
            </form>
        )
    }
}

export { LoginRegisterBox };