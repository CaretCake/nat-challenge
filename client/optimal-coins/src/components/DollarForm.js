import React, {Component} from 'react';
import axios from 'axios';

class DollarForm extends Component {
    constructor(props) {
        super(props);
        this.state = {value: ''};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert('A dollar amount was submitted: ' + this.state.value);
        event.preventDefault();

        axios.get('http://127.0.0.1:5000/api/v1/coins?dollaramount=' + this.state.value)
            .then(response => this.props.handleDollarChange(response.data));
        
    }

    render() {
        return (
        <form onSubmit={this.handleSubmit}>
            <label>
            Dollar Amount:
            <input type="text" value={this.state.value} onChange={this.handleChange} />
            </label>
            <input type="submit" value="Submit" />
        </form>
        );
    }
}

export { DollarForm }