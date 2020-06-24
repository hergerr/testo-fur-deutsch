import "./login-register-box.styles.css"
import { LabelAndInput } from "../label-and-input/label-and-input.component.jsx"
import React from "react"
import axios from 'axios';

class LoginRegisterBox extends React.Component {
    constructor(props) {
        super(props);

        this.state = { login: '', password: '' };
    }

    handleSubmit = event => {
        event.preventDefault();

        axios.post(`http://127.0.0.1:8000/lol/`, { username: this.state.login, password: this.state.password })
        .then(res => {
          console.log(res);
          console.log(res.data);
        })

    }

    handleLoginChange = event => {
        this.setState({ login: event.target.value });
    }

    handlePasswordChange = event => {
        this.setState({ password: event.target.value });
    }

    render() {
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