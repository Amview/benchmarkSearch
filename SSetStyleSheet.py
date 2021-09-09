def setStyleSheet(self):
    self.setStyleSheet('''
                QPushButton#nextPage,#upPage,#endPage,#firstPage{
                    background-color:  #F7F7F7;
                    color:  #000;
                    border: 1px solid  #DADADA;
                    border-radius: 8px;
                    padding: 2px 4px;
                }
                QLabel#labelOn,#labelTotal{
                    background-color:  #F7F7F7;
                    color:  #000;
                    border: 1px solid  #DADADA;
                    border-radius: 8px;
                    padding: 2px 4px;
                }
                QPushButton#singleScore,#search,#updateScore,#gpuScore,#dScore{
                    background-color:  #F7F7F7;
                    color:  #000;
                    border: 1px solid  #DADADA;
                    border-radius: 8px;
                    padding: 2px 4px;
                } 
            ''')
    self.pushButton_close.setStyleSheet(
        '''QPushButton{background:#F76677;border-radius:9px;border:none;}QPushButton:hover{background:rgb(253,88,88);}''')
    self.pushButton_visit.setStyleSheet(
        '''QPushButton{background:#F7D674;border-radius:9px;border:none;}QPushButton:hover{background:rgb(253,189,48);}''')
    self.pushButton_mini.setStyleSheet(
        '''QPushButton{background:#6DDF6D;border:none;border-radius:9px;}QPushButton:hover{background:rgb(54,208,66);}''')
    self.right_widget.setStyleSheet('''
       QWidget{
           border-bottom-right-radius:10px;
           border-left:1px solid #D7D7D7;
           background-color:#F6F6F6;
           }
       QLabel#labelTable{
           border: none;
           background-color:  #F7F7F7;
           color:  #000;
       }
       QPushButton:hover{
           background-color:  #DDEBF7;
           color:  #000;
           border: 1px solid  #DADADA;
           border-radius: 8px;
           padding: 2px 4px;
       } 
       QPushButton:pressed{
           background-color:  #DDEBF7;
           color:  #D1D1D1;
           border: 1px solid  #DADADA;
           border-radius: 8px;
           padding: 2px 4px;
       }   
       QProgressBar{
           border: 1px solid #d7d7d7;
           border-radius:5px;
           background-color:#f6f6f6;
       }
       QProgressBar::chunk{
           width:10px;
           background-color:#c5e1f8;
           margin:0.5px;
       }
       ''')
    self.k_widget.setStyleSheet('''
       QWidget{background:#FFF;
       border-top-right-radius:10px;
       border-bottom:1px solid #D7D7D7;}
       ''')
    self.t_widget.setStyleSheet('''
       QWidget{
           background:#FFF;
           padding:10px;
           border-bottom:1px solid #D7D7D7;
           border-top-left-radius:10px;}
       ''')
    # background:#F4F5F5;
    self.lineEdit.setStyleSheet('''
       QLineEdit{
           background-color:#F7F7F7;
               color:#000;
               border: 1px solid #DADADA;
               border-radius: 8px;
               padding:2px 4px;}
       ''')
    self.h1_widget.setStyleSheet('''
       border:none;
   ''')
    self.horizontal_widget.setStyleSheet('''
       border:none;
   ''')
    self.tableWidget.setStyleSheet('''
       border:none;
       QTableWidget::item{
           selection-background-color:#dadada;
           }
       QHeaderView::section { 
           background-color: #EFEFEF;
            border: none;}
           ''')
    self.tableWidget.verticalScrollBar().setStyleSheet('''
       QScrollBar{
           background:#EFEFEF; 
           width: 8px;
       }
       QScrollBar::handle{
           background:#EFEFEF; 
           width: 8px;
           border-radius: 8px;
       }
       ''')
    self.tableWidget.horizontalHeader().setStyleSheet('''
       QHeaderView::section {
           background-color: #F6F6F6;
           padding-left: 1px;
           border: none;}
       ''')
    self.tableWidget1.setStyleSheet('''
       border:none;
       QTableWidget::item{
           selection-background-color:#dadada;
           }
       QHeaderView::section { 
           background-color: #EFEFEF;
            border: none;}
           ''')
    self.tableWidget1.verticalScrollBar().setStyleSheet('''
       QScrollBar{
           background:#EFEFEF; 
           width: 8px;
       }
       QScrollBar::handle{
           background:#EFEFEF; 
           width: 8px;
           border-radius: 8px;
       }
       ''')
    self.tableWidget1.horizontalHeader().setStyleSheet('''
       QHeaderView::section {
           background-color: #F6F6F6;
           padding-left: 1px;
           border: none;}
       ''')
    # rgb(199, 185, 161)
    # rgb(170, 170, 127)
    self.listWidget.setStyleSheet('''
       background-color: #F6F6F6;
       border-bottom-left-radius:10px;
       color:black;
       font-size:15px;
       ''')
