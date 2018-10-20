import '../sass/app.scss';
import React from "react";
import ReactDOM from "react-dom";
import {MDCRipple} from "@material/ripple/index";
const ripple = new MDCRipple(document.querySelector('.foo-button'));

import {MDCDrawer} from "@material/drawer/index";
const drawer = MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));

import {MDCTopAppBar} from "@material/top-app-bar/index";
const topAppBar = MDCTopAppBar.attachTo(document.getElementById('app-bar'));
topAppBar.listen('MDCTopAppBar:nav', () => {
  drawer.open = !drawer.open;
});

const listEl = document.querySelector('.mdc-drawer .mdc-list');
const mainContentEl = document.querySelector('.main-content');

listEl.addEventListener('click', (event) => {
  drawer.open = false;
});

document.body.addEventListener('MDCDrawer:closed', () => {
  mainContentEl.querySelector('input, button').focus();
});


class Layout extends React.Component {
	constructor() {
		super();
		this.name= "will";
	}
	render() {
		return (
			<h1>It's {this.name}!</h1>
		);
	}
}

const app = document.getElementById('app');

ReactDOM.render(<Layout/>, app)