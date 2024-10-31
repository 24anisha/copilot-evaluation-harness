import * as React from 'react';
import * as ReactDOM from 'react-dom';
import NotificationSystem from 'react-notification-system';
import IToastFactory from './IToastFactory';
import ToastPosition from './ToastPosition';
import ToastParams from './ToastParams';

let notificationSystem = null;



const idify = (notification: ToastParams, id: string) => {
	// Get notification DOM element and stick an id to it.
	const refs = { refs: {} };
	const containerElement = notificationSystem.refs[`container-${notification.position}`] || refs;
	const notificationElement = containerElement.refs[`notification-${notification.id}`] || refs;
	const notificationNode = ReactDOM.findDOMNode(notificationElement);

	if (notificationNode) {
		const toastId = ['toast', notification.level, id];
		notificationNode.setAttribute('id', toastId.join('-'));
	}
};

class Toast implements IToastFactory {
	
	private buildToast (level: string, params: ToastParams | string): void {
		const options = typeof params === 'string'
			? { message: params }
			: params;

		if (!options.message) {
			return;
		}
		
		const obj = Object.assign({}, new ToastParams(level), options);

		if (!notificationSystem) {
			const element = document.createElement('div');
			const wrapper = document.body.appendChild(element);
			element.setAttribute('id', 'notificationSystem');
			notificationSystem = ReactDOM.render(React.createElement(NotificationSystem), wrapper);
		}

		setTimeout(() => {
			const notification = notificationSystem.addNotification(obj);
			console.log(notification);
			// idify(notification, obj.id);
		});		
	}

	info (params: ToastParams | string): void { this.buildToast('info', params); }

    success (params: ToastParams | string): void { this.buildToast('success', params); }

    warning (params: ToastParams | string): void { this.buildToast('warning', params); }
	
    error (params: ToastParams | string): void { this.buildToast('error', params); }
	
}

export default new Toast();