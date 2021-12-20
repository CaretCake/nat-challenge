import React, {Component} from 'react'
import {ReactComponent as CoinLogo} from './logo.svg';


class Header extends Component {
    render()
    {
        return (<div className='Header'>
                    <h2>Welcome to</h2>
                    <CoinLogo/>
                </div>);
    }
}

export { Header }