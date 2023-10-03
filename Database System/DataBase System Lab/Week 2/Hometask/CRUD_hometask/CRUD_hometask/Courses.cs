using CRUD_Operations;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CRUD_hometask
{
    public partial class Courses : Form
    {
        public Courses()
        {
            InitializeComponent();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "" && textBox2.Text != "" && textBox3.Text != "" && textBox4.Text != "" && textBox5.Text != "")
            {
                var con = Configuration.getInstance().getConnection();
                SqlCommand cmd = new SqlCommand("insert into Courses values(@Course_ID,@Course_Name,@Student_Name,@Teacher_Name,@Semester)", con);
                //con.Open();
                cmd.Parameters.AddWithValue("@Course_ID", textBox1.Text);
                cmd.Parameters.AddWithValue("@Course_Name", textBox2.Text);
                cmd.Parameters.AddWithValue("@Student_Name", textBox3.Text);
                cmd.Parameters.AddWithValue("@Teacher_Name", textBox4.Text);
                cmd.Parameters.AddWithValue("@Semester", textBox5.Text);
                cmd.ExecuteNonQuery();
                //con.Close();
                MessageBox.Show("Record Inserted Successfully");
                //DisplayData();
                //ClearData();
            }
            else
            {
                MessageBox.Show("Please Provide Details!");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            var con = Configuration.getInstance().getConnection();
            SqlCommand cmd = new SqlCommand("Select * from Courses", con);
            SqlDataAdapter da = new SqlDataAdapter(cmd);
            DataTable dt = new DataTable();
            da.Fill(dt);
            dataGridView1.DataSource = dt;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "" && textBox2.Text != "" && textBox3.Text != "" && textBox4.Text != "" && textBox5.Text != "")
            {
                var con = Configuration.getInstance().getConnection();
                SqlCommand cmd = new SqlCommand("update Courses set Course_ID=@Course_ID,Course_Name=@Course_Name,Student_Name=@Student_Name,Teacher_Name=@Teacher_Name,Semester=@Semester where Course_ID=@Course_ID", con);
                cmd.Parameters.AddWithValue("@Course_ID", textBox1.Text);
                cmd.Parameters.AddWithValue("@Course_Name", textBox2.Text);
                cmd.Parameters.AddWithValue("@Student_Name", textBox3.Text);
                cmd.Parameters.AddWithValue("@Teacher_Name", textBox4.Text);
                cmd.Parameters.AddWithValue("@Semester", textBox5.Text);
                cmd.ExecuteNonQuery();
                MessageBox.Show("Record Updated Successfully");

            }
            else
            {
                MessageBox.Show("Please Select Record to Update");
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (int.Parse(textBox1.Text) != 0)
            {
                var con = Configuration.getInstance().getConnection();
                SqlCommand cmd = new SqlCommand("delete Courses where Course_ID=@Course_ID", con);
                cmd.Parameters.AddWithValue("@Course_ID", textBox1.Text);
                cmd.ExecuteNonQuery();
                MessageBox.Show("Record Deleted Successfully!");

            }
            else
            {
                MessageBox.Show("Please Select Record to Delete");
            }
        }

        private void dataGridView1_RowHeaderMouseClick(object sender, DataGridViewCellMouseEventArgs e)
        {
            textBox1.Text = dataGridView1.Rows[e.RowIndex].Cells[0].Value.ToString();
            textBox2.Text = dataGridView1.Rows[e.RowIndex].Cells[1].Value.ToString();
            textBox3.Text = dataGridView1.Rows[e.RowIndex].Cells[2].Value.ToString();
            textBox4.Text = dataGridView1.Rows[e.RowIndex].Cells[3].Value.ToString();
            textBox5.Text = dataGridView1.Rows[e.RowIndex].Cells[4].Value.ToString();
        }

        private void textBox6_TextChanged(object sender, EventArgs e)
        {
            var con = Configuration.getInstance().getConnection();
            SqlDataAdapter adapt = new SqlDataAdapter("select * from Courses where Course_ID like '" + textBox1.Text + "%'", con);
            DataTable dt = new DataTable();
            adapt.Fill(dt);
            dataGridView1.DataSource = dt;
        }
    }
}
