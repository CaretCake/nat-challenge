import React, {Component} from 'react';

class CoinCount extends Component {
    render()
    {
        return (
            <div className='CoinContainer'>
                {this.props.silver_dollar}
                {this.props.half_dollar}
                {this.props.quarter}
                {this.props.dime}
                {this.props.nickel}
                {this.props.penny}
            </div>
        );
    }
}

export { CoinCount }