import React from 'react';

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