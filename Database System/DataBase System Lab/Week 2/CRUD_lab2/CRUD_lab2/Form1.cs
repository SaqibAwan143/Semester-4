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

namespace CRUD_lab2
{
    public partial class Form1 : Form
    {
        
        public Form1()
        {
            InitializeComponent();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "" && textBox2.Text != "" && textBox3.Text != "")
            {
                var con = Configuration.getInstance().getConnection();
                SqlCommand cmd = new SqlCommand("Insert into student values (@ID, @Name,@Department)", con);
                cmd.Parameters.AddWithValue("@ID", int.Parse(textBox1.Text));
                cmd.Parameters.AddWithValue("@Name", textBox2.Text);
                cmd.Parameters.AddWithValue("@Department", textBox3.Text);
                cmd.ExecuteNonQuery();
                MessageBox.Show("Successfully saved");
            }
            else
            {
                MessageBox.Show("Please Enter a value to create");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            var con = Configuration.getInstance().getConnection();
            SqlCommand cmd = new SqlCommand("Select * from student", con);
            SqlDataAdapter da = new SqlDataAdapter(cmd);
            DataTable dt = new DataTable();
            da.Fill(dt);
            dataGridView1.DataSource = dt;


        }

        private void button3_Click(object sender, EventArgs e)
        {
            
            if (textBox1.Text != "" && textBox2.Text != "" && textBox3.Text != "")
            {
                var con = Configuration.getInstance().getConnection();
                SqlCommand cmd = new SqlCommand("update student set Name=@name,Department=@Department from student where ID=@ID", con);
                cmd.Parameters.AddWithValue("@ID", int.Parse(textBox1.Text));
                cmd.Parameters.AddWithValue("@Name", textBox2.Text);
                cmd.Parameters.AddWithValue("@Department", textBox3.Text);
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
                SqlCommand cmd = new SqlCommand("delete student where ID=@ID", con);
                cmd.Parameters.AddWithValue("@ID", int.Parse(textBox1.Text));
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
        }

        private void button5_Click(object sender, EventArgs e)
        {
            


            /* var conn = Configuration.getInstance().getConnection();
             string cmdText = "SELECT * From student.ID WHERE " + textBox1.Text + " = @ID";
             //using (SqlConnection conn = new SqlConnection(....))
             using (SqlCommand cmd = new SqlCommand(cmdText, conn))
             {
                 //conn.Open();
                 cmd.Parameters.AddWithValue("@ID", textBox1.Text);
                 //da = new DataSet();
                 DataSet ds = new DataSet();
                 SqlDataAdapter da = new SqlDataAdapter(cmd);
                 //da = new SqlDataAdapter(cmd);
                 da.Fill(ds);
                 dataGridView1.DataSource = ds.Tables[0];


             }*/
            /* var con = Configuration.getInstance().getConnection();
             SqlCommand cmd = new SqlCommand("Select * from student.ID where ID=@ID", con);
             SqlDataAdapter da = new SqlDataAdapter(cmd);
             DataTable dt = new DataTable();
             da.Fill(dt);
             dataGridView1.DataSource = dt;*/
        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {
            var con = Configuration.getInstance().getConnection();
            SqlDataAdapter adapt = new SqlDataAdapter("select * from student where ID like '" + textBox4.Text + "%'", con);
            DataTable dt = new DataTable();
            adapt.Fill(dt);
            dataGridView1.DataSource = dt;
            
        }
    }
}
