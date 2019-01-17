import '../sass/app.scss';
import React from "react";
import ReactDOM from "react-dom";
import {MDCRipple} from "@material/ripple/index";
import Layout from "./components/Layout";
import Header from "./components/Header";
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



const header = document.getElementById('app-bar');
const app = document.getElementById('app');

ReactDOM.render(<Header/>, header);
ReactDOM.render(<Layout/>, app);