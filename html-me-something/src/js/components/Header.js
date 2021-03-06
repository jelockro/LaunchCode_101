import React from 'react';

export default class Header extends React.Component {
	constructor() {
		super();
		this.name= "will";
	}
	render() {
		return (
			<div class="mdc-top-app-bar__row">
        		<section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-start">
		            <a href="#" class="material-icons mdc-top-app-bar__navigation-icon">menu</a>
		            <span class="mdc-top-app-bar__title">CryptAI</span>
		        </section>
		        <section class="mdc-top-app-bar__section mdc-top-app-bar__section--align-end" role="toolbar">
					<a href="#" class="material-icons mdc-top-app-bar__action-item" aria-label="Download" alt="Download">file_download</a>
		            <a href="#" class="material-icons mdc-top-app-bar__action-item" aria-label="Print this page" alt="Print this page">print</a>
		            <a href="#" class="material-icons mdc-top-app-bar__action-item" aria-label="Bookmark this page" alt="Bookmark this page">bookmark</a>
		        </section>
        	</div>
		);
	}
}