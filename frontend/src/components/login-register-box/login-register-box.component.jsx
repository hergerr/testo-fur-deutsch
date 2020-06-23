import "./login-register-box.styles.css"
import { LabelAndInput } from "../label-and-input/label-and-input.component.jsx"
import React from "react"

class LoginRegisterBox extends React.Component {
    constructor(props) {
        super(props);

        this.state = { login: '', password: '' };
    }

    handleSubmit = event => {
        event.preventDefault();
        console.log(JSON.stringify({ username: this.state.login, password: this.state.password }))

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            mode: 'no-cors',
            body: JSON.stringify({ username: this.state.login, password: this.state.password })
        };
        fetch('http://localhost:8000/api/auth/token/login/', requestOptions)
            .then(response => console.log(response))
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