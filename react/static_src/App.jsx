/**
 * Created by geoolekom on 26.03.17.
 */

import React from 'react';
import ReactDOM from 'react-dom';

import Layout from 'components/Layout';
import Feed from "./components/feed/Feed";
import MyPage from "./components/my_page/MyPage";
import FriendList from "./components/friends/FriendList";

class App extends React.Component {

    state = {
        user: undefined,
    };

    activeKeyComponent = (key) => {
        switch (key) {
            case 1: return <MyPage/>;
            case 2: return <Feed/>;
            case 3: return <FriendList/>
        }
    };

    render() {
        return <Layout activeKeyComponent={ this.activeKeyComponent } />;
    }

    componentDidMount() {
        // Authenticate
    }
}

ReactDOM.render(
    <App />,
    document.getElementById('root')
);
