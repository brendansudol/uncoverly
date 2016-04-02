import React from 'react';
import ReactDOM from 'react-dom';
 

class Suggest extends React.Component {
  constructor(props) {
    super(props);
    this.state = {input: ''};
    this.change = this.change.bind(this);
    this.submit = this.submit.bind(this);
  }

  change(e) {
    this.setState({ input: e.target.value });
  }

  submit(e) {
    e.preventDefault();
    console.log(this.state);
  }

  render() {
    return (
      <form className="flex mb2">
        <label className="hide">URL</label>
        <input
          type="text"
          className="flex-auto m0 field rounded-left"
          placeholder="URL"
          onChange={this.change}
          value={this.state.input} />
        <button
          type="submit"
          onClick={this.submit}
          className="btn btn-primary rounded-right">Go</button>
      </form>
    )
  }
}
 

ReactDOM.render(<Suggest />, document.getElementById('content'));
