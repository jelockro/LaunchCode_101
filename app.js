import {MDCRipple} from "@material/ripple/index";
import {MDCRipple} from "@material/list";

const list = MDCList.attachTo(document.querySelector('.mdc-list'));
list.wrapFocus = true;
const ripple = new MDCRipple(document.querySelector('.foo-button'));

