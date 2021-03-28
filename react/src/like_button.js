'use strict';

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  handleClick = () => {
    this.setState({ liked: true });
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return (
      <button onClick={this.handleClick}>
        Like
      </button>
    );
  }
}

(function() {
  const domContainer = document.querySelector('#like_button_container');
  ReactDOM.render(<LikeButton />, domContainer);

  const user = {
    firstName: 'Dave',
    lastName: 'J'
  };

  const element = getGreeting(user);
  ReactDOM.render(element, document.getElementById('root'));

  function getGreeting(user) {
    if (user) {
      return <h1>Hello, {formatName(user)}!</h1>;
    }
    return <h1>Hello, Stranger.</h1>;
  }

  function formatName(user) {
    return user.firstName + ' ' + user.lastName;
  }
})();
