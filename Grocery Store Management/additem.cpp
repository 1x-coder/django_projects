#include "additem.h"
#include "ui_additem.h"

AddItem::AddItem(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::AddItem)
{
    ui->setupUi(this);
}

AddItem::~AddItem()
{
    delete ui;
}

void AddItem::Show()
{
    this->show();
}

void AddItem::on_btnAdd_clicked()
{
    ui->lblInfo->setText("");
    QString sName = ui->txtName->text();
    QString sQuantity = ui->txtQuantity->text();
    QString sStatus = ui->cmbStatus->currentText();
    QString sDOP = ui->txtDOP->text();
    QString sDOS = ui->txtDOS->text();
    QString sSellingPrice = ui->txtSellingPrice->text();
    QString sPurchasePrice = ui->txtPurchasePrice->text();

    QSqlQuery query(MyDB::getInstance()->getDBInstance());
    query.clear();
    query.prepare("insert into cppbuzz_items(Name, Quantity, Status, DOP, DOS, SellingPrice, PurchasePrice) values ('" +sName +"','" +sQuantity + "','"+ sStatus + "','" +sDOP + "','"+ sDOS+ "','"+sSellingPrice+ "','"+ sPurchasePrice + "')");

    if(!query.exec())
    {
        qDebug() << query.lastError().text() << query.lastQuery();
        ui->lblInfo->setText("Unable to Add Item");
    }
    else
    {
        if(query.numRowsAffected() > 0)
        {
            qDebug() <<"read was successful "<< query.lastQuery();
            ui->lblInfo->setText("Item Added Successfully!");
            resetElements();
        }
        else
            qDebug() <<"Unable to Add new Item";
     }

}

void AddItem::resetElements()
{
    ui->txtName->clear();
    ui->txtQuantity->clear();
    ui->txtDOP->clear();
    ui->txtDOS->clear();
    ui->txtSellingPrice->clear();
    ui->txtPurchasePrice->clear();
}
