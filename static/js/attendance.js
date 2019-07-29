// css style to align text to the center of it's container
var Align = {
    textAlign: 'center',
  };
  
  var StudentAttendanceForm = React.createClass({
     
    render: function(){
      return (
      <div>
       <form id="attendance_form" className="form-signin" method="post" action="/here">
          <h2 className="form-signin-heading" style={Align}>Submit Attendance</h2>
  
          <div className="form-group has-success">
            <label htmlFor="course" className="sr-only">Course</label>
            <input type="text" id="course" name="course" className="form-control" placeholder="Enter course code here" />
          </div>

          <div className="form-group has-success">
            <label htmlFor="keyword" className="sr-only">Keyword</label>
            <input type="text" id="keyword" name="keyword" className="form-control" placeholder="Enter keyword here" />
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