// css style to align text to the center of it's container
var Align = {
    textAlign: 'center',
  };
  
  var origin = window.location.origin;

  var StudentAttendanceForm = React.createClass({
    
    //don't need this
    getInitialState: function(){
      // set initial state of form inputs
      return {title: '', option: '', options: []}
    },
  
    handleCourseChange: function(e){
      //change title as the user types
      this.setState({course: e.target.value});
    },
  
    handleKeywordChange: function(e){
      this.setState({keyword: e.target.value});
    },
  
    //don't need this
    handleOptionAdd: function(e){
      //update poll options and reset options to an empty string
      this.setState({
      options: this.state.options.concat({name: this.state.option}),
      option: ''
      });
    },

    handleSubmit: function(e){
      e.preventDefault();

      var user = this.state.user //this is undefined
      var course = this.state.course
      var keyword = this.state.keyword

      var data = {'user': user, 'course': course, 'keyword': keyword}
      
      var url = origin + '/api/attendance'

      $.ajax({
        url: url,
        dataType: 'json',
        type: 'POST',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        success: function(data){
          alert(data.message);
        }.bind(this),
        error: function(xhr, status, err){
          alert('Attendance submit failed: ' + err.toString());
        }.bind(this)
      });
    },
  
    render: function(){
      return (
      <div>
       <form id="attendance_form" className="form-signin" onSubmit={this.handleSubmit}>
          <h2 className="form-signin-heading" style={Align}>Submit Attendance</h2>
  
          <div className="form-group has-success">
            <label htmlFor="course" className="sr-only">Course</label>
            <input type="text" id="course" name="course" className="form-control" placeholder="Enter course code here" onChange={this.handleCourseChange}
            value={this.state.course ? this.state.course: ''} required autoFocus />
          </div>

          <div className="form-group has-success">
            <label htmlFor="keyword" className="sr-only">Keyword</label>
            <input type="text" id="keyword" name="keyword" className="form-control" placeholder="Enter keyword here" onChange={this.handleKeywordChange}
            value={this.state.keyword ? this.state.keyword: ''} required autoFocus />
          </div>
  
          <div className="row form-group">
            <button className="btn btn-lg btn-success btn-block" type="submit">I'm Here!</button>
          </div>
          <br />
        </form>
      </div>
      );
    }
  });
    
  ReactDOM.render(
    <div>
      <StudentAttendanceForm />
    </div>,
    document.getElementById('form_container')
  );