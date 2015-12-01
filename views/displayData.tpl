% rebase('layout.tpl', title='Display Data', year=year)
<div class="jumbotron">
	<form  action="/displayData" method="post" class="form-horizontal" role="form">
	<div class="form-group pull-right">
      <div class="col-sm-offset-2 col-sm-10" >
        <!-- <input value="Current Progress"  type="submit" name="Accept" class="btn btn-primary active"/> -->
      </div>
    </div>
	</form>
  <h2>FHIR User Observation</h2>
	<table class="table">
			<thead>
				<tr>
						<th data-field="date">Date</th>
						<th data-field="steps">Steps</th>
				</tr>
			</thead>

			<tbody>
				% for observation in observations_pretty:
				<tr>
					<td>{{observation['date']}}</td>
					<td>{{observation['value']}}</td>
				</tr>
				% end
			</tbody>
		</table>


		<hr>
    <pre style="border-left: medium solid; padding-left: 1em; display:table">
			<h3>Raw data for grading purposes</h3>
			{{observations_raw}}
		</pre>

</div>
