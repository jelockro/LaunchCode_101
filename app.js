import {MDCRipple} from "@material/ripple/index";
const ripple = new MDCRipple(document.querySelector('.foo-button'));

import {MDCList} from "@material/list/index";
const list = MDCList.attachTo(document.querySelector('.mdc-list'));
list.wrapFocus = true;

import {MDCDrawer} from "@material/drawer/index";
const drawer = MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));



