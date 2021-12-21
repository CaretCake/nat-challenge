import React, {Component} from 'react'
import {ReactComponent as CoinLogo} from '../assets/logo.svg';


class Header extends Component {
    render()
    {
        return (<div className='header'>
                    <div className='logo-container'>
                        <CoinLogo/>
                    </div>
                    <h1>Opti<span>Change</span></h1>
                </div>);
    }
}

export { Header }