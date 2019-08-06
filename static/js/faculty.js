// css style to align text to the center of it's container
var Align = {
    textAlign: 'center',
  };
  
  var FacultyAttendanceForm = React.createClass({
    
    handleSubmit: function(e) {
      //
    },

    render: function(){
      return (
      <div>
       <form id="faculty_form" className="form-signin" method="post" action="/searchattend">
          <h2 className="form-signin-heading" style={Align}>Search Attendance</h2>
  
          <div className="form-group has-success">
            <label htmlFor="course" className="sr-only">Course</label>
            <input type="text" id="course" name="course" className="form-control" placeholder="Enter course code here" />
          </div>
  
          <div className="form-group has-success">
            <label htmlFor="course" className="sr-only">Section</label>
            <input type="text" id="section" name="section" className="form-control" placeholder="Enter course section here" />
          </div>

          <div className="form-group has-success">
            <label htmlFor="keyword" className="sr-only">Keyword</label>
            <input type="text" id="keyword" name="keyword" className="form-control" placeholder="Enter keyword here" />
          </div>
  
          <div className="row form-group">
            <button className="btn btn-lg btn-success btn-block" type="submit">Search</button>
          </div>
          <br />
        </form>

        <h3 style={Align}>Attendance Records</h3>

      </div>
      );
    }
  });
    
  ReactDOM.render(
    <div>
      <FacultyAttendanceForm />
    </div>,
    document.getElementById('form_container')
  );