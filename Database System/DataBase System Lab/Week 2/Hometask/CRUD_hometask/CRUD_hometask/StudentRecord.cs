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
    public partial class StudentRecord : Form
    {
        public StudentRecord()
        {
            InitializeComponent();
            
        }
        private void button1_Click_1(object sender, EventArgs e)
        {
            if (textBox1.Text != "" && textBox2.Text != "" && textBox3.Text != "" && textBox4.Text != "" && textBox5.Text != "")
            {
                var con = Configuration.getInstance().getConnection();
                SqlCommand cmd = new SqlCommand("insert into StuRecord values(@RegNumber,@Name,@Department,@Session,@Address)", con);
                //con.Open();
                cmd.Parameters.AddWithValue("@RegNumber", textBox1.Text);
                cmd.Parameters.AddWithValue("@Name", textBox2.Text);
                cmd.Parameters.AddWithValue("@Department", textBox3.Text);
                cmd.Parameters.AddWithValue("@Session", int.Parse(textBox4.Text));
                cmd.Parameters.AddWithValue("@Address", textBox5.Text);
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

        private void button2_Click_1(object sender, EventArgs e)
        {
            var con = Configuration.getInstance().getConnection();
            SqlCommand cmd = new SqlCommand("Select * from StuRecord", con);
            SqlDataAdapter da = new SqlDataAdapter(cmd);
            DataTable dt = new DataTable();
            da.Fill(dt);
            dataGridView1.DataSource = dt;
        }

        private void button3_Click_1(object sender, EventArgs e)
        {

            if (textBox1.Text != "" && textBox2.Text != "" && textBox3.Text != "" && textBox4.Text != "" && textBox5.Text != "")
            {
                var con = Configuration.getInstance().getConnection();
                SqlCommand cmd = new SqlCommand("update StuRecord set Name=@Name,Department=@Department,Session=@Session,Address=@Address where RegNumber=@RegNumber", con);
                cmd.Parameters.AddWithValue("@RegNumber", textBox1.Text);
                cmd.Parameters.AddWithValue("@Name", textBox2.Text);
                cmd.Parameters.AddWithValue("@Department", textBox3.Text);
                cmd.Parameters.AddWithValue("@Session", int.Parse(textBox4.Text));
                cmd.Parameters.AddWithValue("@Address", textBox5.Text);
                cmd.ExecuteNonQuery();
                MessageBox.Show("Record Updated Successfully");

            }
            else
            {
                MessageBox.Show("Please Select Record to Update");
            }
        }

        private void button4_Click_1(object sender, EventArgs e)
        {
            if (int.Parse(textBox1.Text) != 0)
            {
                var con = Configuration.getInstance().getConnection();
                SqlCommand cmd = new SqlCommand("delete StuRecord where RegNumber=@RegNumber", con);
                cmd.Parameters.AddWithValue("@RegNumber", textBox1.Text);
                cmd.ExecuteNonQuery();
                MessageBox.Show("Record Deleted Successfully!");

            }
            else
            {
                MessageBox.Show("Please Select Record to Delete");
            }
        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

        private void dataGridView1_RowHeaderMouseClick_1(object sender, DataGridViewCellMouseEventArgs e)
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
            SqlDataAdapter adapt = new SqlDataAdapter("select * from StuRecord where RegNumber like '" + textBox1.Text + "%'", con);
            DataTable dt = new DataTable();
            adapt.Fill(dt);
            dataGridView1.DataSource = dt;
        }
    }
}
