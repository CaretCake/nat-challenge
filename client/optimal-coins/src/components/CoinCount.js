import React, {Component} from 'react';
import {ReactComponent as SilverCoin} from '../assets/silver-coin.svg';
import {ReactComponent as CopperCoin} from '../assets/copper-coin.svg';

class CoinCount extends Component {
    render()
    {
        return (
            <div className='coin-container'>
                <div className="coin">
                    <div className='coin-info'>
                        <SilverCoin/>
                        Silver Dollar
                        <span className='coin-counter'>{this.props.silver_dollar}</span>
                    </div>
                </div>
                <div className="coin">
                    <div className='coin-info'>
                        <SilverCoin/>
                        Half Dollar
                        <span className='coin-counter'>{this.props.half_dollar}</span>
                    </div>
                </div>
                <div className="coin">
                    <div className='coin-info'>
                        <SilverCoin/>
                        Quarter
                        <span className='coin-counter'>{this.props.quarter}</span>
                    </div>
                </div>
                <div className="coin">
                    <div className='coin-info'>
                        <SilverCoin/>
                        Dime
                        <span className='coin-counter'>{this.props.dime}</span>
                    </div>
                </div>
                <div className="coin">
                    <div className='coin-info'>
                        <SilverCoin/>
                        Nickel
                        <span className='coin-counter'>{this.props.nickel}</span>
                    </div>
                    
                </div>
                <div className="coin">
                    <div className='coin-info'>
                        <CopperCoin/>
                        Penny
                        <span className='coin-counter'>{this.props.penny}</span>
                    </div>
                </div>
            </div>
        );
    }
}

export { CoinCount }