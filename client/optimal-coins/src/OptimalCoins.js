import React, {Component} from 'react';
import { DollarForm } from './DollarForm.js'
import { CoinCount } from './CoinCount.js'

class OptimalCoins extends Component {
    constructor(props) {
        super(props);
        this.handleDollarChange = this.handleDollarChange.bind(this);
        this.state = {silver_dollar: '', half_dollar: '', quarter: '', dime: '', nickel: '', penny: ''};
    }

    handleDollarChange(coins) {
        console.log(coins);
        this.setState({
            silver_dollar: coins['silver-dollar'],
            half_dollar: coins['half-dollar'],
            quarter: coins['quarter'],
            dime: coins['dime'],
            nickel: coins['nickel'],
            penny: coins['penny'],
        });
    }

    render() {
        const silver_dollar = this.state.silver_dollar;
        const half_dollar = this.state.half_dollar;
        const quarter = this.state.quarter;
        const dime = this.state.dime;
        const nickel = this.state.nickel;
        const penny = this.state.penny;

        return(
            <div className='content'>
                <DollarForm
                    handleDollarChange={this.handleDollarChange} />
                <CoinCount
                    silver_dollar={silver_dollar}
                    half_dollar={half_dollar}
                    quarter={quarter}
                    dime={dime}
                    nickel={nickel}
                    penny={penny} />
            </div>
        );
    }
}

export { OptimalCoins }